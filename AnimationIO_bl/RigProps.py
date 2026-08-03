import bpy

class SfRigBoneProperties(bpy.types.PropertyGroup):
    twist_bone_driver_name: bpy.props.StringProperty(name="Driver Name", default="INVALID")
    twist_bone_driver_weight: bpy.props.FloatProperty(name="Driver weight", default=0.0, min=0.0, soft_max=1.0)
    do_correct_bone: bpy.props.BoolProperty(name="Correct bone axes", default=False, description="On export, AnimationIO corrects bone axes with if the checkmark is on. If you're experiencing axis-related problem, uncheck it on specific bones.")
    bone_type: bpy.props.EnumProperty(
        name="Bone type",
        default="Default",
        items=[
            ("Default", "Default", "Default bone"),
            ("Twist", "Twist", "Twist bone"),
        ]
    )
    lod_value: bpy.props.IntProperty(name="LOD Value", default=0)
    mapping: bpy.props.EnumProperty(
        name="Bone Map",
        default="255",
        items=[
            ("0", "Root", "Mapped as Root"),
            ("1", "AnimObjectA", "Mapped as AnimObjectA"),
            ("2", "AnimObjectB", "Mapped as AnimObjectB"),
            ("3", "AnimObjectC", "Mapped as AnimObjectC"),
            ("4", "AnimObjectD", "Mapped as AnimObjectD"),
            ("5", "Camera", "Mapped as Camera"),
            ("6", "Camera_Control", "Mapped as Camera_Control"),
            ("7", "CamTargetParent", "Mapped as CamTargetParent"),
            ("8", "CameraTarget", "Mapped as CameraTarget"),
            ("9", "COM", "Mapped as COM"),
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
    is_mannequin: bpy.props.BoolProperty(name="Is mannequin", default=False)

_classes = [
SfRigBoneProperties,
SfRigProperties,
]

def register():
    for c in _classes:
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

def unregister():
    for c in _classes:
        bpy.utils.unregister_class(c)

    o = bpy.types.Object
    b = bpy.types.EditBone

    del o.sf_rig_props
    del b.sf_bone_props