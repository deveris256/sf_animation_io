import os

import bpy
from enum import Enum

from AnimationIO.AnimatableRig import get_rig_ptr_and_rig, create_rig_armature, bl_import_anim_from_path
from CommonUtils import gen_description_box, GetRigByName, GetRigReferenceObject, ensure_object_mode, \
    deselect_all_objects, ensure_bl_mode_on_obj, rig_list_enum_items, gstr, worked, spawn_error, set_object_armature

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

class AnimationImportMode:
    def __init__(self, imp_mode, selected_rig): # todo requested flags in init and it validates that
        """
        Valid import modes:
        as_armature
        as_armature_with_reference
        on_active_object
        """
        active_obj = bpy.context.view_layer.objects.active

        self.obj_name = None
        self.import_on = None
        self.ref_obj_path = GetRigReferenceObject(selected_rig)

        # {deveris} removed len of files, I need to handle that
        if imp_mode == "on_active_object"and\
            active_obj is not None and\
            active_obj.type in ["MESH", "ARMATURE"]:

            self.obj_name = bpy.context.view_layer.objects.active.name
            self.import_on = active_obj.type

        elif imp_mode == "as_armature_with_reference" and self.ref_obj_path != None:
            existing_objs = set(bpy.context.scene.objects)
            bpy.ops.import_scene.fbx(filepath=self.ref_obj_path, use_anim=False) # use_anim is false not to import fbx armature.
            objs = [o.name for o in list(set(bpy.context.scene.objects) - existing_objs)]
            armatures_list = [o for o in objs if bpy.data.objects.get(o).type == "ARMATURE"]
            bpy.data.batch_remove([bpy.data.objects.get(o) for o in armatures_list])
            objs = [o for o in objs if o not in armatures_list]
            self.obj_name = objs[0]
            self.import_on = "MESH"
            if len(objs) > 1: # join ref objects to one
                with bpy.context.temp_override(
                        active_object=bpy.data.objects.get(objs[0]),
                        selected_editable_objects=[bpy.data.objects.get(o) for o in objs]):
                    bpy.ops.object.join()

    def __repr__(self):
        return f"obj name {self.obj_name}\nimport on {self.import_on}\nref obj path {self.ref_obj_path}"

class ImportCustomAnimation(bpy.types.Operator):
    bl_idname = "import_scene.custom_af"
    bl_label = "Import Custom Animation"

    bl_options = {'UNDO'}

    filepath: bpy.props.StringProperty(options={'HIDDEN'})
    directory: bpy.props.StringProperty(options={'HIDDEN'})
    files: bpy.props.CollectionProperty(type=bpy.types.OperatorFileListElement)
    filename: bpy.props.StringProperty(default='untitled.af')
    filter_glob: bpy.props.StringProperty(default="*.af", options={'HIDDEN'})

    selected_rig: bpy.props.EnumProperty(name="Rig", items=rig_list_enum_items)

    imp_mode: bpy.props.EnumProperty(
        name="Mode",
        items=[
            ("as_armature", "As Armature", "Imports animation as new armature with no further action"),
            ("as_armature_with_reference", "Armature with reference", "Imports animation as new armature while adding reference object (if registered alongside rig)"),
            ("on_active_object", "On active object", "Replaces animation of armature if active object is armature, or adds armature and replaces/adds armature modifier of the object if the object is mesh."),
        ],
        default="as_armature")

    set_frames_end: bpy.props.BoolProperty(name="Set Frames End", default=True)

    def draw(self, context):
        layout = self.layout

        box = layout.box()
        box.prop(self, "selected_rig")
        gen_description_box(self.strings["selected_rig"], box)

        box = layout.box()

        if len(self.files) > 1 and self.imp_mode == "on_active_object":
            abox = box.box()
            abox.alert = True
            abox.label(text="Multiple files selected", icon='WARNING_LARGE')
            abox.label(text="Won't import on active object")

        box.prop(self, "imp_mode")
        gen_description_box(self.strings["on_active_object"], box)

        box = layout.box()
        box.prop(self, "set_frames_end")
        gen_description_box(self.strings["set_frames_end"], box)

    def validate_execute(self, files):
        if self.selected_rig == "NONE":
            raise Exception(f"Please register before importing (F3 -> Register Starfield Rig)")

        if len(files) == 0:
            raise Exception("No .af files to import")

    def execute(self, context):
        files = [f for f in self.files
                 if os.path.isfile(os.path.join(self.directory, f.name))
                 and f.name.lower().endswith(".af")]

        did_not_work = worked(self.validate_execute, [files])

        if did_not_work:
            spawn_error(self, did_not_work)
            return {'CANCELLED'}

        imp_mode = AnimationImportMode(self.imp_mode, self.selected_rig)
        max_frames = 0

        ensure_object_mode()
        deselect_all_objects()

        rig_path = GetRigByName(self.selected_rig)
        rig_ptr, rig = get_rig_ptr_and_rig(rig_path)

        # If armature is active and import is on active object
        if imp_mode.import_on == "ARMATURE":
            orig_armature_obj = bpy.context.scene.objects.get(imp_mode.obj_name)
            orig_armature_obj.animation_data_clear()
            ensure_bl_mode_on_obj("POSE", orig_armature_obj)

            for b in rig.bones:
                bone = orig_armature_obj.pose.bones.get(b.name)
                bone.matrix_basis.identity()

        # if not then proceed create armature
        else:
            orig_armature_obj = create_rig_armature(rig)
            ensure_bl_mode_on_obj("POSE", orig_armature_obj)

        ensure_object_mode()

        # Import all sel file
        for file in files:
            filepath = os.path.join(self.directory, file.name)
            filename = os.path.basename(filepath)[:-3]

            if file != files[-1]:
                armature_obj = orig_armature_obj.copy()
                armature_obj.data = orig_armature_obj.data.copy()
                bpy.context.collection.objects.link(armature_obj)
                armature_obj.animation_data_clear()

                if imp_mode.obj_name is not None:
                    _obj_for_ref = bpy.data.objects.get(imp_mode.obj_name)
                    ref_obj = _obj_for_ref.copy()
                    ref_obj.data = _obj_for_ref.data.copy()
                    ref_obj.name = f"{filename}_refobj"
                    bpy.context.collection.objects.link(ref_obj)
            else:
                armature_obj = orig_armature_obj

                if imp_mode.obj_name is not None:
                    ref_obj = bpy.data.objects.get(imp_mode.obj_name)
                    ref_obj.name = f"{filename}_refobj"

            anim_name = file.name.rpartition(".")[0]
            print("bl_import_anim_from_path")
            bl_import_anim_from_path(filepath, rig, rig_path, armature_obj)

            armature_obj.data.name = anim_name
            armature_obj.name = anim_name

            max_keyframe_idx = 0
            for b in rig.bones:
                if len(b.matrix._overlay_matrices.keys()) > 0:
                    max_keyframe_idx = max((max_keyframe_idx, max(b.matrix._overlay_matrices.keys())))

            if max_keyframe_idx > max_frames:
                max_frames = max_keyframe_idx

            ensure_object_mode()

            # If import active on mesh, then set armature modifier
            if imp_mode.obj_name == "MESH":
                set_object_armature(
                    filename,
                    ref_obj.name,
                    armature_obj.name
                )

        if self.set_frames_end:
            bpy.context.scene.frame_end = max_frames

        return {'FINISHED'}
    def invoke(self, context, event):
        self.strings = gstr(strings)
        context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}

def menu_func_anim_import(self, context):
    self.layout.operator(
        ImportCustomAnimation.bl_idname,
        text="Starfield Animation (.af)",
    )

_classes_ = [
    ImportCustomAnimation,
]

def register():
    for c in _classes_: bpy.utils.register_class(c)

    bpy.types.VIEW3D_MT_view.append(menu_func_anim_import)

def unregister():
    for c in _classes_: bpy.utils.unregister_class(c)

    bpy.types.VIEW3D_MT_view.remove(menu_func_anim_import)
