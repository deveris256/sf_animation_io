import bpy

from CommonUtils import gen_pretty_prop_table, gen_description_box, gen_pretty_prop_table_with_label


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
        box.label(text="Rig utils")
        row = box.row()
        row.operator("scene.register_custom_rig", text="Reg. Rig from file")
        #TODO: row.operator("scene.register_custom_reference_object", text="Reg. reference")

        if not obj or obj.type != "ARMATURE":
            layout.label(text="Select armature object")
            return

        layout.prop(obj.sf_rig_props, "is_rig", text="Is Rig")
        layout.prop(obj.sf_anim_props, "is_anim", text="Is Animation")

        if not obj.sf_rig_props.is_rig:
            col = layout.column()
            gen_description_box(["Active object is not", "a Starfield rig."], col, 0.5)
            return

def obj_get_bone_name_by_name(name, obj):
    bones = [b.name for b in obj.data.edit_bones if b.name == name]
    if len(bones) == 0:
        return "INVALID"
    return bones[0]

# todo: ability to set props for all menu's visible bones.
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
            gen_pretty_prop_table_with_label(box, bone.sf_bone_props, {
                # TODO: missing properties. Should skip index, though.
                #"index": ["Index", None, {}, None],
                #"mirror_name": ["Mirror", ObjGetBoneNameByIndex, {"obj": obj}, None],
                "lod_value": ["LOD", None, {}, None],
                "bone_type": ["Type", None, {}, None],
            }, space_for_icons=False)

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
            gen_pretty_prop_table_with_label(box, bone.sf_bone_props, {
                "twist_bone_driver_name": ["Driver name", obj_get_bone_name_by_name, {"obj": obj}, None],
                "twist_bone_driver_weight": ["Driver weight", None, {}, None],
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

        # TODO: Validation.
        #layout.operator(ValidateCustomAnimation.bl_idname)

        layout.prop(obj.sf_anim_props, "anim_name", text="Name")

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

        gen_pretty_prop_table(layout, obj.sf_rig_props, {
            "rig_name": ["Name", None],
            "rig_precision": ["Precision", None],
        }, space_for_icons=False)

_classes = [
OBJECT_PT_SF_AnimationManagementPanel,
OBJECT_PT_SF_AnimationManagementPanel_AnimationMode,
OBJECT_PT_SF_AnimationManagementPanel_RigMode,
OBJECT_PT_SF_AnimationManagementPanel_BoneMode,
OBJECT_PT_SF_AnimationManagementPanel_BoneMapMode,
OBJECT_PT_SF_AnimationManagementPanel_TwistBoneMode,
]

def register():
    for c in _classes:
        bpy.utils.register_class(c)

    c = bpy.types.Scene
    c.sf_show_all_bones = bpy.props.BoolProperty(
        name="Show all selected",
        default=False
    )

def unregister():
    for c in _classes:
        bpy.utils.unregister_class(c)

    c = bpy.types.Scene
    del c.sf_show_all_bones