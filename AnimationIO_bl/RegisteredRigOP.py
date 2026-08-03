import bpy
import os
import shutil

from AnimationIO import AnimatableRig
from CommonUtils import (
    GetRigFolder,
    prepare_file_name, gen_description_box, ensure_object_mode, ensure_bl_mode_on_obj)


def register_rig_file(rig_path, rig_name):
    source_path = rig_path
    destination_path = os.path.join(GetRigFolder(), f"{rig_name}.rig")
    shutil.copyfile(source_path, destination_path)

def UpdateRigName(self, context):
    self["rig_name"] = prepare_file_name(self.rig_name.lower().removesuffix(".rig"))

class OpenRegisteredRigsFolder(bpy.types.Operator):
    bl_idname = "scene.sf_open_registered_rigs_folder"
    bl_label = "Open registered rigs folder"

    bl_options = {'REGISTER'}

    def execute(self, context):
        import os
        folder = GetRigFolder()
        if os.path.isdir(folder):
            os.startfile(folder)
        else:
            raise Exception(f"Not a folder: {folder}")
        return {'FINISHED'}

class RegisterCustomRig(bpy.types.Operator):
    bl_idname = "scene.register_custom_rig"
    bl_label = "Register Starfield Rig From File"

    bl_options = {'REGISTER'}

    filepath: bpy.props.StringProperty(options={'HIDDEN'})
    filename: bpy.props.StringProperty(default='untitled.rig')
    filter_glob: bpy.props.StringProperty(default="*.rig", options={'HIDDEN'})

    rig_name: bpy.props.StringProperty(
        name="Name",
        description="Name the Rig should be registered as",
        update=UpdateRigName
    )

    @classmethod
    def poll(cls, context):
        return True

    def draw(self, context):
        s = self.strings
        layout = self.layout

        rig_name = prepare_file_name(self.rig_name.lower().removesuffix(".rig"))

        box = layout.box()

        # Alert on overwrite checks
        if rig_name in self.existing_rigs:
            alert_box = box.box()

        if not rig_name:
            no_name_alert = box.box()
            no_name_alert.alert = True
            no_name_alert.label(text="Rig must have a name", icon='WARNING_LARGE')

        box.prop(self, "rig_name")

        # Alert on overwrite checks
        if rig_name in self.existing_rigs:
            alert_box.alert = True
            alert_box.label(text="OVERWRITING EXISTING RIG:", icon='WARNING_LARGE')
            alert_box.label(text=f"{rig_name}.rig")

        gen_description_box(s["rig_name"], box)

        row = layout.row()
        row.label(text="")
        row.scale_y = 0.5
        layout.label(text=f"Existing Rigs ({self.rig_amount}):")
        layout.operator('scene.sf_open_registered_rigs_folder')

        for name in self.existing_rigs:
            box = layout.box()
            row = box.row()
            row.label(text=name)
            row.scale_y = 0.5

    def execute(self, context):
        self.rig_name = prepare_file_name(self.rig_name.lower().removesuffix(".rig"))
        if not self.rig_name:
            self.report({'ERROR'}, f"Rig name cannot be empty")
            return {'CANCELLED'}

        if not os.path.isfile(self.filepath):
            self.report({'ERROR'}, f"Unable to register rig: File does not exist: {self.filepath}")
            return {'CANCELLED'}

        register_rig_file(self.filepath, self.rig_name)
        self.report({'INFO'}, "Successfully registered rig")
        return {'FINISHED'}

_classes = [
OpenRegisteredRigsFolder,
RegisterCustomRig,
]

def menu_func_register_rig(self, context):
    self.layout.operator(
        RegisterCustomRig.bl_idname,
        text="Register Starfield Rig (.rig)",
    )

def register():
    for c in _classes:
        bpy.utils.register_class(c)

    bpy.types.VIEW3D_MT_view.append(menu_func_register_rig)
    # TODO:
    #bpy.types.TOPBAR_MT_file_import.append(menu_func_rig_import)
    #bpy.types.TOPBAR_MT_file_export.append(menu_func_rig_export)

def unregister():
    for c in _classes:
        bpy.utils.unregister_class(c)

    bpy.types.VIEW3D_MT_view.remove(menu_func_register_rig)
    # TODO:
    #bpy.types.TOPBAR_MT_file_import.remove(menu_func_rig_import)
    #bpy.types.TOPBAR_MT_file_export.remove(menu_func_rig_export)