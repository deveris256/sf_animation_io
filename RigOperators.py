import bpy
import os
import textwrap
from API import AnimConverter, RigUtils
from CommonUtils import PrepareFileName, GenDescriptionBox

strings = {
    "rig_name": \
        "A name the Rig should be registered as - "
        "for example, \"human_male\". "
        "You will see the name in UI when importing animation. "
        "If rig with the same name already exists, new rig will overwrite it. "
        "Do not include file extension."
}

def gstr():
    new_strings = {}
    for name, info in strings.items():
        info = info.strip().replace("\n", " ")
        info = textwrap.wrap(info, width=35)
        new_strings.update({name: info})
    return new_strings

class ExportCustomRig(bpy.types.Operator):
    bl_idname = "export_scene.export_custom_starfield_rig"
    bl_label = "Starfield Rig (.rig)"

    bl_options = {'REGISTER', 'UNDO'}

    filepath: bpy.props.StringProperty(options={'HIDDEN'})
    filename: bpy.props.StringProperty(default='untitled.rig')
    filter_glob: bpy.props.StringProperty(default="*.rig", options={'HIDDEN'})

    def execute(self, context):
        if context.object.type != "ARMATURE":
            self.report({'ERROR'}, "Not an armature")
            return
        if not context.object.sf_rig_props.is_rig:
            self.report({'ERROR'},"Not marked as Starfield rig")
            return

        bpy.ops.object.mode_set(mode='EDIT')
        AnimConverter.ExportRig(context.object, self.filepath)
        bpy.ops.object.mode_set(mode='OBJECT')

        self.report({'INFO'}, "Exported rig successfully.")
        return {'FINISHED'}

    def invoke(self, context, event):
        context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}

class ImportCustomRig(bpy.types.Operator):
    bl_idname = "import_scene.import_custom_starfield_rig"
    bl_label = "Starfield Rig (.rig)"

    bl_options = {'REGISTER', 'UNDO'}

    filepath: bpy.props.StringProperty(options={'HIDDEN'})
    filename: bpy.props.StringProperty(default='untitled.rig')
    filter_glob: bpy.props.StringProperty(default="*.rig", options={'HIDDEN'})

    def execute(self, context):
        rig = AnimConverter.ImportRig(self.filepath)

        armature_data = bpy.data.armatures.new(name="armature")
        armature_obj = bpy.data.objects.new(name="armature_obj", object_data=armature_data)
        bpy.context.collection.objects.link(armature_obj)
        bpy.ops.object.select_all(action='DESELECT')
        bpy.context.view_layer.objects.active = armature_obj
        bpy.ops.object.mode_set(mode='EDIT')
        RigUtils.RecursiveCreateRig(armature_obj, rig, [b for b in rig.bones if b.parent_name == None])
        RigUtils.RigPostProcess(armature_obj)
        RigUtils.RigSetBoneAttr(rig, armature_obj)
        bpy.ops.object.mode_set(mode='OBJECT')

        rig.SetArmatureAttributes(armature_obj)
        return {'FINISHED'}

    def invoke(self, context, event):
        context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}

class RegisterCustomRig(bpy.types.Operator):
    bl_idname = "scene.register_custom_rig"
    bl_label = "Register Starfield Rig From File"

    bl_options = {'REGISTER'}

    filepath: bpy.props.StringProperty(options={'HIDDEN'})
    filename: bpy.props.StringProperty(default='untitled.rig')
    filter_glob: bpy.props.StringProperty(default="*.rig", options={'HIDDEN'})

    rig_name: bpy.props.StringProperty(
        name="Name",
        description="Name the Rig should be registered as"
    )

    @classmethod
    def poll(cls, context):
        return True

    def draw(self, context):
        s = self.strings
        layout = self.layout

        rig_name = PrepareFileName(self.rig_name.lower().removesuffix(".rig"))

        box = layout.box()

        # Alert on overwrite checks
        if rig_name in self.existing_rigs:
            alert_box = box.box()

        box.prop(self, "rig_name")

        # Alert on overwrite checks
        if rig_name in self.existing_rigs:
            alert_box.alert = True
            alert_box.label(text="OVERWRITING EXISTING RIG:", icon='WARNING_LARGE')
            alert_box.label(text=f"{rig_name}.rig")

        GenDescriptionBox(s["rig_name"], box)

        row = layout.row()
        row.label(text="")
        row.scale_y = 0.5
        layout.label(text=f"Existing Rigs ({self.rig_amount}):")

        for name in self.existing_rigs:
            box = layout.box()
            row = box.row()
            row.label(text=name)
            row.scale_y = 0.5

    def execute(self, context):
        self.rig_name = PrepareFileName(self.rig_name.lower().removesuffix(".rig"))
        if not os.path.isfile(self.filepath):
            self.report({'ERROR'}, f"Unable to register rig: File does not exist: {self.filepath}")
            return {'CANCELLED'}

        RigUtils.RegisterRigFile(self.filepath, self.rig_name)
        self.report({'INFO'}, "Successfully registered rig")
        return {'FINISHED'}

    def invoke(self, context, event):
        self.filename = "skeleton.rig"
        context.window_manager.fileselect_add(self)
        self.strings = gstr()
        self.existing_rigs = RigUtils.GetExistingRigs()
        self.rig_amount = len(self.existing_rigs)
        if len(self.existing_rigs) == 0:
            self.existing_rigs.append("NO RIGS FOUND")
        return {'RUNNING_MODAL'}

class SfRigProperties(bpy.types.PropertyGroup):
    is_rig: bpy.props.BoolProperty(name="Is rig", default=False)
    rig_name: bpy.props.StringProperty(name="Rig name")
    rig_precision: bpy.props.EnumProperty(
        name="Rig Precision",
        default="DEFAULT",
        items=[
            ("DEFAULT", "DEFAULT", "Rig precision found to be used in regular rigs"),
            ("FIRST_PERSON", "FIRST_PERSON", "Rig precision found to be used in first person rigs"),
            ("SHIP", "SHIP", "Rig precision found to be used in ship rigs"),
        ]
    )
    validation_errors: bpy.props.StringProperty(name="Errors", default="")

class SfRigBoneProperties(bpy.types.PropertyGroup):
    index: bpy.props.IntProperty(name="Index", default=-1, min=0)
    mirror_index: bpy.props.IntProperty(name="Mirror index", default=-1, min=-1)
    twist_bone_driver_index: bpy.props.IntProperty(name="Driver index", default=-1, min=-1)
    twist_bone_driver_weight: bpy.props.FloatProperty(name="Driver weight", default=0.0, min=0.0, soft_max=1.0)
    bone_type: bpy.props.EnumProperty(
        name="Bone type",
        default="Default",
        items=[
            ("Default", "Default", "Default bone"),
            ("Twist", "Twist", "Twist bone"),
        ]
    )
    mapping: bpy.props.EnumProperty(
        name="Bone type",
        default="255",
        items=[
            ("0",  "Root","Mapped as Root"),
            ("1",  "AnimObjectA","Mapped as AnimObjectA"),
            ("2",  "AnimObjectB","Mapped as AnimObjectB"),
            ("3",  "AnimObjectC","Mapped as AnimObjectC"),
            ("4",  "AnimObjectD","Mapped as AnimObjectD"),
            ("5",  "Camera","Mapped as Camera"),
            ("6",  "Camera_Control","Mapped as Camera_Control"),
            ("7",  "CamTargetParent","Mapped as CamTargetParent"),
            ("8",  "CameraTarget","Mapped as CameraTarget"),
            ("9",  "COM","Mapped as COM"),
            ("10", "C_Hips", "Mapped as C_Hips"),
            ("11", "R_Thigh", "Mapped as R_Thigh"),
            ("12", "R_Calf", "Mapped as R_Calf"),
            ("13", "R_Foot", "Mapped as R_Foot"),
            ("14", "R_Toe", "Mapped as R_Toe"),
            ("19", "L_Thigh", "Mapped as L_Thigh"),
            ("20", "L_Calf", "Mapped as L_Calf"),
            ("21", "L_Foot", "Mapped as L_Foot"),
            ("22", "L_Toe", "Mapped as L_Toe"),
            ("29", "C_Spine", "Mapped as C_Spine"),
            ("30", "C_Spine1", "Mapped as C_Spine1"),
            ("31", "C_Spine2", "Mapped as C_Spine2"),
            ("32", "C_Chest", "Mapped as C_Chest"),
            ("33", "C_Neck", "Mapped as C_Neck"),
            ("34", "C_Neck1", "Mapped as C_Neck1"),
            ("35", "C_Head", "Mapped as C_Head"),
            ("39", "L_Clavicle", "Mapped as L_Clavicle"),
            ("40", "L_Biceps", "Mapped as L_Biceps"),
            ("41", "L_Forearm", "Mapped as L_Forearm"),
            ("42", "L_Wrist", "Mapped as L_Wrist"),
            ("43", "L_Thumb", "Mapped as L_Thumb"),
            ("44", "L_Thumb1", "Mapped as L_Thumb1"),
            ("45", "L_Thumb2", "Mapped as L_Thumb2"),
            ("46", "L_Cup", "Mapped as L_Cup"),
            ("47", "L_Pinky", "Mapped as L_Pinky"),
            ("48", "L_Pinky1", "Mapped as L_Pinky1"),
            ("49", "L_Pinky2", "Mapped as L_Pinky2"),
            ("50", "L_Ring", "Mapped as L_Ring"),
            ("51", "L_Ring1", "Mapped as L_Ring1"),
            ("52", "L_Ring2", "Mapped as L_Ring2"),
            ("53", "L_Middle", "Mapped as L_Middle"),
            ("54", "L_Middle1", "Mapped as L_Middle1"),
            ("55", "L_Middle2", "Mapped as L_Middle2"),
            ("56", "L_Index", "Mapped as L_Index"),
            ("57", "L_Index1", "Mapped as L_Index1"),
            ("58", "L_Index2", "Mapped as L_Index2"),
            ("59", "L_AnimObject1", "Mapped as L_AnimObject1"),
            ("60", "L_AnimObject2", "Mapped as L_AnimObject2"),
            ("61", "L_AnimObject3", "Mapped as L_AnimObject3"),
            ("62", "L_Arm", "Mapped as L_Arm"),
            ("64", "L_Elbow", "Mapped as L_Elbow"),
            ("68", "C_BackPack", "Mapped as C_BackPack"),
            ("69", "C_BackPackHose", "Mapped as C_BackPackHose"),
            ("72", "R_Clavicle", "Mapped as R_Clavicle"),
            ("73", "R_Biceps", "Mapped as R_Biceps"),
            ("74", "R_Forearm", "Mapped as R_Forearm"),
            ("75", "R_Wrist", "Mapped as R_Wrist"),
            ("76", "R_Thumb", "Mapped as R_Thumb"),
            ("77", "R_Thumb1", "Mapped as R_Thumb1"),
            ("78", "R_Thumb2", "Mapped as R_Thumb2"),
            ("79", "R_Cup", "Mapped as R_Cup"),
            ("80", "R_Pinky", "Mapped as R_Pinky"),
            ("81", "R_Pinky1", "Mapped as R_Pinky1"),
            ("82", "R_Pinky2", "Mapped as R_Pinky2"),
            ("83", "R_Ring", "Mapped as R_Ring"),
            ("84", "R_Ring1", "Mapped as R_Ring1"),
            ("85", "R_Ring2", "Mapped as R_Ring2"),
            ("86", "R_Middle", "Mapped as R_Middle"),
            ("87", "R_Middle1", "Mapped as R_Middle1"),
            ("88", "R_Middle2", "Mapped as R_Middle2"),
            ("89", "R_Index", "Mapped as R_Index"),
            ("90", "R_Index1", "Mapped as R_Index1"),
            ("91", "R_Index2", "Mapped as R_Index2"),
            ("92", "R_AnimObject1", "Mapped as R_AnimObject1"),
            ("93", "R_AnimObject2", "Mapped as R_AnimObject2"),
            ("94", "R_AnimObject3", "Mapped as R_AnimObject3"),
            ("95", "R_Arm", "Mapped as R_Arm"),
            ("97", "R_Elbow", "Mapped as R_Elbow"),
            ("101", "Weapon", "Mapped as Weapon"),
            ("119", "Bolt01", "Mapped as Bolt01"),
            ("120", "Bolt02", "Mapped as Bolt02"),
            ("134", "WeaponLeft", "Mapped as WeaponLeft"),
            ("137", "DirectAt", "Mapped as DirectAt"),
            ("140", "C_Waist", "Mapped as C_Waist"),
            ("141", "Camera_Control_FP", "Mapped as Camera_Control_FP"),
            ("142", "R_Thigh_Twist", "Mapped as R_Thigh_Twist"),
            ("143", "R_Thigh_Twist1", "Mapped as R_Thigh_Twist1"),
            ("144", "L_Thigh_Twist", "Mapped as L_Thigh_Twist"),
            ("145", "L_Thigh_Twist1", "Mapped as L_Thigh_Twist1"),
            ("146", "C_Neck_Twist", "Mapped as C_Neck_Twist"),
            ("147", "L_Wrist_Twist", "Mapped as L_Wrist_Twist"),
            ("148", "L_Wrist_Twist1", "Mapped as L_Wrist_Twist1"),
            ("149", "L_Wrist_Twist2", "Mapped as L_Wrist_Twist2"),
            ("150", "L_Biceps_Twist", "Mapped as L_Biceps_Twist"),
            ("151", "L_Biceps_Twist1", "Mapped as L_Biceps_Twist1"),
            ("152", "R_Wrist_Twist", "Mapped as R_Wrist_Twist"),
            ("153", "R_Wrist_Twist1", "Mapped as R_Wrist_Twist1"),
            ("154", "R_Wrist_Twist2", "Mapped as R_Wrist_Twist2"),
            ("155", "R_Biceps_Twist", "Mapped as R_Biceps_Twist"),
            ("156", "R_Biceps_Twist1", "Mapped as R_Biceps_Twist1"),
            ("255", "None", "Mapped as Unknown Mapping"),
        ]
    )


__classes__ = [
    SfRigBoneProperties,
    SfRigProperties,
    RegisterCustomRig,
    ImportCustomRig,
    ExportCustomRig,
]

def menu_func_register_rig(self, context):
    self.layout.operator(
        RegisterCustomRig.bl_idname,
        text="Register Starfield Rig (.rig)",
    )

def menu_func_rig_import(self, context):
    self.layout.operator(
        ImportCustomRig.bl_idname,
        text="Starfield Rig (.rig)",
    )

# TODO
def menu_func_rig_export(self, context):
    self.layout.operator(
        ExportCustomRig.bl_idname,
        text="Starfield Rig (.rig)",
    )

def register():
    for c in __classes__:
        bpy.utils.register_class(c)

    o = bpy.types.Object
    b = bpy.types.EditBone

    o.sf_rig_props = bpy.props.PointerProperty(
        name="Starfield rig properties",
        type=SfRigProperties
    )

    b.sf_bone_props = bpy.props.PointerProperty(
        name="Starfield rig bone properties",
        type=SfRigBoneProperties
    )

    bpy.types.VIEW3D_MT_view.append(menu_func_register_rig)
    bpy.types.TOPBAR_MT_file_import.append(menu_func_rig_import)
    bpy.types.TOPBAR_MT_file_export.append(menu_func_rig_export)

def unregister():
    for c in __classes__:
        bpy.utils.unregister_class(c)

    bpy.types.VIEW3D_MT_view.remove(menu_func_register_rig)
    bpy.types.TOPBAR_MT_file_import.remove(menu_func_rig_import)
    bpy.types.TOPBAR_MT_file_export.remove(menu_func_rig_export)
