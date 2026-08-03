import bpy
import os

from AnimationIO.AnimatableRig import bl_import_rig_from_path

class ImportCustomRig(bpy.types.Operator):
    bl_idname = "import_scene.import_custom_starfield_rig"
    bl_label = "Starfield Rig (.rig)"

    bl_options = {'REGISTER', 'UNDO'}

    filepath: bpy.props.StringProperty(options={'HIDDEN'})
    filename: bpy.props.StringProperty(default='untitled.rig')
    filter_glob: bpy.props.StringProperty(default="*.rig", options={'HIDDEN'})

    def execute(self, context):
        if not os.path.isfile(self.filepath) or not self.filepath.lower().endswith(".rig"):
            self.report({'ERROR'}, f"Not a rig file: {self.filepath}")
            return {'CANCELLED'}

        bl_import_rig_from_path(self.filepath)

        return {'FINISHED'}

    def invoke(self, context, event):
        context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}


def menu_func_rig_import(self, context):
    self.layout.operator(
        ImportCustomRig.bl_idname,
        text="Starfield Rig (.rig)",
    )

_classes = [
ImportCustomRig,
]

def register():
    for c in _classes:
        bpy.utils.register_class(c)

    bpy.types.VIEW3D_MT_view.append(menu_func_rig_import)

def unregister():
    for c in _classes:
        bpy.utils.unregister_class(c)

    bpy.types.VIEW3D_MT_view.remove(menu_func_rig_import)
