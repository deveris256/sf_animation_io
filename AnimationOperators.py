import os
import textwrap

import bpy

from API import AnimConverter
from API.AnimationUtils import LoadAnim
from CommonUtils import GenDescriptionBox, PrepareFileName, GenPrettyPropTable, GenPrettyPropTableWithLabel
from API.RigUtils import (
    rig_list_enum_items,
    GetRigByName, RecursiveCreateRig, RigPostProcess, RigSetBoneAttr)

strings = {
    "selected_rig": \
        "Corresponding animation's matching rig. "
        "If the rig doesn't match, the animation won't export!",
    "on_active_object": \
        "Imports animation and replaces/creates an armature "
        "modifier for an active object (if found)",
    "set_frames_end": \
        "Sets the ending frame of the scene to the ending "
        "frame of the imported animation."
}

def gstr():
    new_strings = {}
    for name, info in strings.items():
        info = info.strip().replace("\n", " ")
        info = textwrap.wrap(info, width=35)
        new_strings.update({name: info})
    return new_strings

class ImportCustomAnimation(bpy.types.Operator):
    bl_idname = "import_scene.custom_af"
    bl_label = "Import Custom Animation"

    filepath: bpy.props.StringProperty(options={'HIDDEN'})
    directory: bpy.props.StringProperty(options={'HIDDEN'})
    files: bpy.props.CollectionProperty(type=bpy.types.OperatorFileListElement)
    filename: bpy.props.StringProperty(default='untitled.af')
    filter_glob: bpy.props.StringProperty(default="*.af", options={'HIDDEN'})

    selected_rig: bpy.props.EnumProperty(name="Rig", items=rig_list_enum_items)

    on_active_object: bpy.props.BoolProperty(name="On Active Object", default=False)

    set_frames_end: bpy.props.BoolProperty(name="Set Frames End", default=True)

    def draw(self, context):
        layout = self.layout

        box = layout.box()
        box.prop(self, "selected_rig")
        GenDescriptionBox(self.strings["selected_rig"], box)

        box = layout.box()
        box.prop(self, "on_active_object")
        GenDescriptionBox(self.strings["on_active_object"], box)

        box = layout.box()
        box.prop(self, "set_frames_end")
        GenDescriptionBox(self.strings["set_frames_end"], box)

    def execute(self, context):
        m = bpy.context.view_layer.objects.active
        mesh_obj_name = None

        if self.on_active_object and m != None and m.type == "MESH" and len(self.files) == 1:
            mesh_obj_name = bpy.context.view_layer.objects.active.name
        else:
            self.on_active_object = False

        if self.selected_rig == "NONE":
            self.report({'ERROR'}, f"Please register rig first (F3 -> Register Starfield Rig)")
            return {'CANCELLED'}

        rig_path = GetRigByName(self.selected_rig)

        if rig_path == None:
            self.report({'ERROR'}, f"Rig doesn't exist: {self.selected_rig}")
            return {'CANCELLED'}

        max_frames = 0

        if bpy.context.object is not None and bpy.context.object.mode != "OBJECT":
            bpy.ops.object.mode_set(mode='OBJECT')

        bpy.ops.object.select_all(action='DESELECT')

        rig = AnimConverter.ImportRig(rig_path)

        orig_armature_data = bpy.data.armatures.new(name="armature")
        orig_armature_obj = bpy.data.objects.new(name=rig.name, object_data=orig_armature_data)
        bpy.context.collection.objects.link(orig_armature_obj)

        bpy.context.view_layer.objects.active = orig_armature_obj
        bpy.ops.object.mode_set(mode='EDIT')
        RecursiveCreateRig(orig_armature_obj, rig, [b for b in rig.bones if b.parent_name == None])
        RigPostProcess(orig_armature_obj)
        RigSetBoneAttr(rig, orig_armature_obj)
        bpy.ops.object.mode_set(mode='OBJECT')

        bpy.context.scene.frame_set(0)

        for file in self.files:
            filepath = os.path.join(self.directory, file.name)
            anim_scene = AnimConverter.ImportAnimation(rig_path, filepath)
            anim_data = anim_scene.animations[0]

            if file != self.files[-1]:
                armature_obj = orig_armature_obj.copy()
                armature_obj.data = orig_armature_obj.data.copy()
                bpy.context.collection.objects.link(armature_obj)
            else:
                armature_obj = orig_armature_obj

            armature_obj.data.name = anim_data.name
            armature_obj.name = anim_data.name

            rig.SetArmatureAttributes(armature_obj)

            bpy.ops.object.mode_set(mode='POSE')
            for frame_idx, frame in anim_data.frames.items():
                target_frame = int(frame_idx)

                LoadAnim(
                    armature_obj,
                    target_frame,
                    frame.bone_data
                )

            if len(anim_data.frames.keys()) > max_frames:
                max_frames = len(anim_data.frames.keys())

            bpy.ops.object.mode_set(mode='OBJECT')
            anim_scene.SetAnimationAttributes(armature_obj)
            anim_data.SetAnimationAttributes(armature_obj)

        bpy.context.scene.frame_set(0)

        if self.set_frames_end:
            bpy.context.scene.frame_end = max_frames

        if mesh_obj_name != None:
            mod_name = self.filepath[0][:-3]
            mesh_obj = bpy.context.scene.objects.get(mesh_obj_name)
            mods = [m for m in mesh_obj.modifiers if m.type == 'ARMATURE']
            if len(mods) == 0:
                modifier = mesh_obj.modifiers.new(name=mod_name, type='ARMATURE')
            else:
                modifier = mods[0]

            modifier.name = mod_name
            modifier.use_deform_preserve_volume = False
            modifier.use_multi_modifier = False
            modifier.object = armature_obj
            modifier.use_vertex_groups = True
            modifier.use_bone_envelopes = False

            mesh_obj.parent = armature_obj

        return {'FINISHED'}

    def invoke(self, context, event):
        self.strings = gstr()
        context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}

class ValidateCustomAnimation(bpy.types.Operator):
    bl_idname = "object.sf_validate_anim"
    bl_label = "Validate Animation"

    warnings: bpy.props.StringProperty(name="Input Text", default="")

    def draw(self, context):
        layout = self.layout

        for warn in self.warnings.split("\n"):
            row = layout.row()
            row.label(text=warn)
            row.scale_y = 0.5

    def execute(self, context):
        return {'FINISHED'}

    def invoke(self, context, event):
        obj = context.object
        bpy.ops.object.select_all(action='DESELECT')
        bpy.context.view_layer.objects.active = obj

        if not obj.type == "ARMATURE":
            self.warnings += "Object is not an armature\n"
        else:
            twist_with_keyframe = []
            bpy.ops.object.mode_set(mode='EDIT')

            for bone in [b for b in context.object.data.edit_bones if b.sf_bone_props.bone_type == "Twist"]:
                for fk in obj.animation_data.action.fcurves:
                    if bone.name in twist_with_keyframe: continue
                    if fk.data_path.startswith(f'pose.bones["{bone.name}"]'):
                        twist_with_keyframe.append(bone.name)
                        self.warnings += f"{bone.name} type is Twist, but keyframe is found.\n"
            bpy.ops.object.mode_set(mode='OBJECT')
        return context.window_manager.invoke_props_dialog(self)


class ExportCustomAnimation(bpy.types.Operator):
    bl_idname = "export_scene.custom_af"
    bl_label = "Export Custom Animation"

    filepath: bpy.props.StringProperty(options={'HIDDEN'})
    filename: bpy.props.StringProperty(default='untitled.af')
    filter_glob: bpy.props.StringProperty(default="*.af", options={'HIDDEN'})

    selected_rig: bpy.props.EnumProperty(name="Rig", items=rig_list_enum_items)

    def draw(self, context):
        layout = self.layout
        rigs = [r for r in bpy.context.selected_objects if r.type == "ARMATURE" and r.sf_anim_props.is_anim]

        box = layout.box()
        box.prop(self, "selected_rig")
        GenDescriptionBox(self.strings["selected_rig"], box)

        if len(rigs) == 0:
            box = layout.box()
            box.alert = True
            col = box.column()
            col.scale_y = 0.7
            col.label(text="⚠ No animation armature selected.")
            col.label(text="Nothing will be exported.")
            col.label(text="Mark armature as Animation in")
            col.label(text="the Animation IO tab")
        elif len(rigs) == 1:
            layout.label(text=f"Exporting {rigs[0].name}")
        else:
            box = layout.box()
            box.alert = True
            box.label(text=f"⚠ Filename box will be ignored")
            layout.label(text=f"These files will be exported:")
            col = layout.column()
            col.scale_y = 0.7
            [col.label(text=r.sf_anim_props.anim_name + ".af") for r in rigs]


    def execute(self, context):

        rigs = [r for r in bpy.context.selected_objects if r.type == "ARMATURE" and r.sf_anim_props.is_anim]

        if len(rigs) == 0:
            self.report({'ERROR'}, f"Select armature(s) marked as Animation in Animation IO tab")
            return {'CANCELLED'}

        for rig_obj in rigs:
            bpy.ops.object.select_all(action='DESELECT')

            rig_path = GetRigByName(self.selected_rig)

            if len(rigs) == 1:
                path = self.filepath
            else:
                path = os.path.join(os.path.dirname(self.filepath), PrepareFileName(rig_obj.sf_anim_props.anim_name) + ".af")

            if rig_path == None:
                self.report({'ERROR'}, f"Rig doesn't exist: {self.selected_rig}")
                return {'CANCELLED'}
            if rig_obj == None:
                self.report({'ERROR'}, f"Please select an armature")
                return {'CANCELLED'}
            if not rig_obj.sf_anim_props.is_anim:
                self.report({'ERROR'}, f"Please mark it as animation")
                return {'CANCELLED'}
            elif not rig_obj.type == "ARMATURE":
                self.report({'ERROR'}, f"Not an armature: {rig_obj.name}")
                return {'CANCELLED'}

            ## pose mode
            bpy.context.view_layer.objects.active = rig_obj
            bpy.ops.object.mode_set(mode='POSE')
            AnimConverter.ExportAnimation(
                path,
                rig_obj,
                rig_path
            )

            bpy.ops.object.mode_set(mode='OBJECT')

        return {'FINISHED'}

    def invoke(self, context, event):
        self.strings = gstr()
        self.filename = f"{context.object.name if context.object != None else 'UNKNOWN'}.af"

        if context.object != None and context.object.type == "ARMATURE" and context.object.sf_rig_props.rig_name in [r[0] for r in rig_list_enum_items(self, context)]:
            self.selected_rig = context.object.sf_rig_props.rig_name

        context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}

class OBJECT_PT_SF_AnimationManagementPanel_BoneMapMode(bpy.types.Panel):
    bl_idname = "OBJECT_PT_SF_AnimationManagementPanel_BoneMapMode"
    bl_label = "Bone Mapping"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Starfield Animation Management"
    bl_parent_id = "OBJECT_PT_SF_AnimationManagementPanel"

    @classmethod
    def poll(self, context):
        obj = context.object
        return obj is not None and obj.sf_rig_props.is_rig and obj.mode == "EDIT"

    def draw(self, context):
        layout = self.layout
        obj = context.object

        if obj.data.edit_bones.active == None:
            return

        bone_list = [b for b in obj.data.edit_bones]

        for bone in bone_list:
            box = layout.box()
            row = box.row()
            row.label(text=bone.name)
            row.prop(bone.sf_bone_props, "mapping", text="")

class OBJECT_PT_SF_AnimationManagementPanel_BoneMode(bpy.types.Panel):
    bl_idname = "OBJECT_PT_SF_AnimationManagementPanel_BoneMode"
    bl_label = "Bone Editor"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Starfield Animation Management"
    bl_parent_id = "OBJECT_PT_SF_AnimationManagementPanel"

    @classmethod
    def poll(self, context):
        obj = context.object
        return obj is not None and obj.sf_rig_props.is_rig and obj.mode == "EDIT"

    def draw(self, context):
        layout = self.layout
        obj = context.object

        layout.prop(context.scene, "sf_show_all_bones")

        if obj.data.edit_bones.active == None:
            return

        if context.scene.sf_show_all_bones:
            bone_list = [b for b in obj.data.edit_bones if b.select]
        else:
            bone_list = [obj.data.edit_bones.active]

        for bone in bone_list:
            box = layout.box()
            box.label(text=bone.name)
            GenPrettyPropTableWithLabel(box, bone.sf_bone_props, {
                "index": ["Index", None, {}, None],
                "mirror_index": ["Mirror", ObjGetBoneNameByIndex, {"obj": obj}, None],
                "bone_type": ["Type", None, {}, None],
            }, space_for_icons=False)

class OBJECT_PT_SF_AnimationManagementPanel_TwistBoneMode(bpy.types.Panel):
    bl_idname = "OBJECT_PT_SF_AnimationManagementPanel_TwistBoneMode"
    bl_label = "Twist Bone Editor"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Starfield Animation Management"
    bl_parent_id = "OBJECT_PT_SF_AnimationManagementPanel_BoneMode"
    bl_options = {'DEFAULT_CLOSED'}
    @classmethod
    def poll(self, context):
        obj = context.object
        return obj is not None and obj.sf_rig_props.is_rig and obj.mode in ["EDIT"]

    def draw(self, context):
        layout = self.layout
        obj = context.object

        if obj.data.edit_bones.active == None:
            return

        bone_list = []

        if context.scene.sf_show_all_bones:
            bone_list = [b for b in obj.data.edit_bones if b.select and b.sf_bone_props.bone_type == "Twist"]
        elif obj.data.edit_bones.active.sf_bone_props.bone_type == "Twist":
            bone_list = [obj.data.edit_bones.active]

        for bone in bone_list:
            box = layout.box()
            box.label(text=bone.name)
            GenPrettyPropTableWithLabel(box, bone.sf_bone_props, {
                "twist_bone_driver_index": ["Driver index", ObjGetBoneNameByIndex, {"obj": obj}, None],
                "twist_bone_driver_weight": ["Driver weight", None, {}, None],
            }, space_for_icons=False)

def ObjGetBoneNameByIndex(index, obj):
    if index in [-1, -2]:
        return "None"

    bones = [b.name for b in obj.data.edit_bones if b.sf_bone_props.index == index]
    if len(bones) == 0:
        return "INVALID"
    return bones[0]

class OBJECT_PT_SF_AnimationManagementPanel_RigMode(bpy.types.Panel):
    bl_idname = "OBJECT_PT_SF_AnimationManagementPanel_RigMode"
    bl_label = "Rig Editor"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Starfield Animation Management"
    bl_parent_id = "OBJECT_PT_SF_AnimationManagementPanel"
    bl_options = {'HEADER_LAYOUT_EXPAND'}

    @classmethod
    def poll(self, context):
        obj = context.object
        return obj is not None and obj.sf_rig_props.is_rig

    def draw(self, context):
        layout = self.layout
        obj = context.object

        GenPrettyPropTable(layout, obj.sf_rig_props, {
            "rig_name": ["Name", None],
            "rig_precision": ["Precision", None],
        }, space_for_icons=False)

class OBJECT_PT_SF_AnimationManagementPanel_AnimationMode(bpy.types.Panel):
    bl_idname = "OBJECT_PT_SF_AnimationManagementPanel_AnimationMode"
    bl_label = "Animation Editor"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Starfield Animation Management"
    bl_parent_id = "OBJECT_PT_SF_AnimationManagementPanel"
    bl_options = {'HEADER_LAYOUT_EXPAND'}

    @classmethod
    def poll(self, context):
        obj = context.object
        return obj is not None and obj.sf_rig_props.is_rig and obj.sf_anim_props.is_anim

    def draw(self, context):
        layout = self.layout
        obj = context.object

        layout.operator(ValidateCustomAnimation.bl_idname)

        layout.prop(obj.sf_anim_props, "anim_name", text="Name")

class OBJECT_PT_SF_AnimationManagementPanel(bpy.types.Panel):
    bl_idname = "OBJECT_PT_SF_AnimationManagementPanel"
    bl_label = "Starfield Animation Management"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Starfield Animation Management"
    bl_options = {'HEADER_LAYOUT_EXPAND'}
    bl_order = 1299

    def draw(self, context):
        layout = self.layout
        obj = context.object

        box = layout.box()
        box.label(text="General")
        box.operator("scene.register_custom_rig")

        if not obj or obj.type != "ARMATURE":
            layout.label(text="Select armature object")
            return

        layout.prop(obj.sf_rig_props, "is_rig", text="Is Rig")
        layout.prop(obj.sf_anim_props, "is_anim", text="Is Animation")

        if not obj.sf_rig_props.is_rig:
            col = layout.column()
            GenDescriptionBox(["Active object is not", "a Starfield rig."], col, 0.5)
            return

class SfAnimProperties(bpy.types.PropertyGroup):
    is_anim: bpy.props.BoolProperty(name="Is animation", default=False)
    anim_name: bpy.props.StringProperty(name="Name", default="UNKNOWN")
    validation_errors: bpy.props.StringProperty(name="Errors", default="")

__classes__ = [
    SfAnimProperties,
    ImportCustomAnimation,
    ExportCustomAnimation,
    ValidateCustomAnimation,
    OBJECT_PT_SF_AnimationManagementPanel,
    OBJECT_PT_SF_AnimationManagementPanel_AnimationMode,
    OBJECT_PT_SF_AnimationManagementPanel_RigMode,
    OBJECT_PT_SF_AnimationManagementPanel_BoneMode,
    OBJECT_PT_SF_AnimationManagementPanel_TwistBoneMode,
    OBJECT_PT_SF_AnimationManagementPanel_BoneMapMode,
]

def menu_func_import(self, context):
    self.layout.operator(
        ImportCustomAnimation.bl_idname,
        text="Starfield Animation (.af)",
    )

def menu_func_export(self, context):
    self.layout.operator(
        ExportCustomAnimation.bl_idname,
        text="Starfield Animation (.af)",
    )

def register():
    for c in __classes__:
        bpy.utils.register_class(c)

    o = bpy.types.Object
    s = bpy.types.Scene

    o.sf_anim_props = bpy.props.PointerProperty(
        name="Starfield animation properties",
        type=SfAnimProperties
    )

    s.sf_show_all_bones = bpy.props.BoolProperty(
        name="Show all selected",
        default=False
    )

    bpy.types.TOPBAR_MT_file_import.append(menu_func_import)
    bpy.types.TOPBAR_MT_file_export.append(menu_func_export)

def unregister():
    for c in __classes__:
        bpy.utils.unregister_class(c)

    o = bpy.types.Object
    s = bpy.types.Scene

    bpy.types.TOPBAR_MT_file_import.remove(menu_func_import)
    bpy.types.TOPBAR_MT_file_export.remove(menu_func_export)

    del o.sf_anim_props
    del s.sf_show_all_bones
