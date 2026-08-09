import json

import bpy
import os

from AnimationIO.AnimatableRig import bl_import_rig_from_path, bl_export_rig_from_path
from CommonUtilsAnimIO import rig_list_existing_bone_order_json_enum_items, get_bone_order


class ExportCustomRig(bpy.types.Operator):
    bl_idname = "export_scene.export_custom_starfield_rig"
    bl_label = "Starfield Rig (.rig)"

    bl_options = {'REGISTER', 'UNDO'}

    filepath: bpy.props.StringProperty(options={'HIDDEN'})
    filename: bpy.props.StringProperty(default='untitled.rig')
    filter_glob: bpy.props.StringProperty(default="*.rig", options={'HIDDEN'})

    selected_bone_order: bpy.props.EnumProperty(name="Bone order", items=rig_list_existing_bone_order_json_enum_items)

    def validate(self):
        pass # todo move validation logic here.

    def draw(self, context):
        layout = self.layout
        box = layout.box()
        box.prop(self, "selected_bone_order")

    def execute(self, context):
        if not self.filepath.lower().endswith(".rig"):
            self.filepath += ".rig"

        rig = bpy.context.view_layer.objects.active
        if rig.type != "ARMATURE":
            self.report({'ERROR'}, f"Please select an armature")
            return {'CANCELLED'}

        bone_order_file = get_bone_order(self.selected_bone_order)
        bone_order = None
        if bone_order_file is not None and os.path.isfile(bone_order_file):
            bone_order = [b.strip() for b in open(bone_order_file).readlines() if b.strip() is not None]
            print(f"Loaded bone order: {bone_order}")

        bl_export_rig_from_path(rig, self.filepath, bone_order=bone_order)

        return {'FINISHED'}

    def invoke(self, context, event):
        context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}


def menu_func_rig_export(self, context):
    self.layout.operator(
        ExportCustomRig.bl_idname,
        text="Starfield Rig (.rig)",
    )

_classes = [
ExportCustomRig,
]

def register():
    for c in _classes:
        bpy.utils.register_class(c)

    bpy.types.VIEW3D_MT_view.append(menu_func_rig_export)

def unregister():
    for c in _classes:
        bpy.utils.unregister_class(c)

    bpy.types.VIEW3D_MT_view.remove(menu_func_rig_export)
