import os

import bpy
import bpy_extras.io_utils

from ..AnimationIO.AnimatableRig import bl_export_anim
from ..CommonUtilsAnimIO import rig_list_enum_items, GetRigByName, worked, spawn_error


class ExportCustomAnimation(bpy.types.Operator, bpy_extras.io_utils.ExportHelper):
    bl_idname = "export_scene.custom_af"
    bl_label = "Export Custom Animation"

    bl_options = {'UNDO'}

    filename_ext = ".af"
    filter_glob: bpy.props.StringProperty(default="*.af", options={'HIDDEN'})

    selected_rig: bpy.props.EnumProperty(name="Rig", items=rig_list_enum_items)

    def draw(self, context):
        layout = self.layout

        box = layout.box()
        box.prop(self, "selected_rig")

    def _validate(self):
        if self.selected_rig == "NONE":
            raise Exception("Please register rig (F3 -> Register Rig)")

        active = bpy.context.view_layer.objects.active

        if active is None or active.type != "ARMATURE":
            raise Exception("Please ensure an armature is a current active object")

    def execute(self, context):
        e = worked(self._validate, {})

        if e: return spawn_error(self, e)

        rig_file = GetRigByName(self.selected_rig)
        rig_obj = bpy.context.view_layer.objects.active

        e = worked(bl_export_anim, {
            "export_path": self.filepath,
            "rig_obj": rig_obj,
            "rig_path": rig_file})

        if e: return spawn_error(self, e)

        return {'FINISHED'}

    def invoke(self, context, event):
        context.window_manager.fileselect_add(self)
        self.filepath += "CustomAnimation.af"
        return {'RUNNING_MODAL'}

def menu_func_anim_import(self, context):
    self.layout.operator(
        ExportCustomAnimation.bl_idname,
        text="Starfield Animation (.af)",
    )

_classes_ = [
    ExportCustomAnimation,
]

def register():
    for c in _classes_: bpy.utils.register_class(c)

    bpy.types.VIEW3D_MT_view.append(menu_func_anim_import)

def unregister():
    for c in _classes_: bpy.utils.unregister_class(c)

    bpy.types.VIEW3D_MT_view.remove(menu_func_anim_import)
