import ctypes

from API.AnimConverterFunc import (
    _LoadSFBGSSkeletonRigFromFileC, _SaveSkeletonRigToSFBGSFormatDirectC,
    _SaveAnimationToSFBGSFormatWithExistingRigDirectC, _DeleteSkeletonRigC,
)
from API.AnimationScene import AnimScene
from API.BlenderSpecificUtils import ensure_object_mode, deselect_all_objects_set_active, ensure_bl_mode_on_obj
from API.SkeletonRig import SkelRig


def LoadRigPtr(rig_path):
    err = ctypes.c_char()
    print("Rig path:", rig_path)
    rigPtr = _LoadSFBGSSkeletonRigFromFileC(
        ctypes.c_wchar_p(rig_path)
    )
    return rigPtr

class Vector3D(ctypes.Structure):
    _fields_ = [
        ("x", ctypes.c_double),
        ("y", ctypes.c_double),
        ("z", ctypes.c_double)
    ]

class Translation(Vector3D):
    _fields_ = [
        ("frame", ctypes.c_uint16)
    ]

def GetAllBoneKeyframes(armature_obj, bone_name):
    action = armature_obj.animation_data.action
    keyframes = []

    loc_keyframes_by_frame = {}
    rot_keyframes_by_frame = {}

    armature_obj.pose.bones.get(bone_name).rotation_mode = 'QUATERNION'

    # The function is unused for now, but for the future -
    # should be made compatible with 5.0
    for fcurve in action.fcurves:
        data_path = fcurve.data_path

        if not data_path.startswith(f'pose.bones[\"{bone_name}\"]'):
            continue

        if data_path.endswith(".location"):
            array_index = fcurve.array_index

            for kp in fcurve.keyframe_points:
                frame = kp.co[0]
                value = kp.co[1]

                if frame not in loc_keyframes_by_frame:
                    loc_keyframes_by_frame[frame] = [0.0, 0.0, 0.0]

                loc_keyframes_by_frame[frame][array_index] = value

        elif data_path.endswith(".rotation_quaternion"):
            array_index = fcurve.array_index

            for kp in fcurve.keyframe_points:
                frame = kp.co[0]
                value = kp.co[1]

                if frame not in rot_keyframes_by_frame:
                    rot_keyframes_by_frame[frame] = [0.0, 0.0, 0.0, 0.0]

                rot_keyframes_by_frame[frame][array_index] = value

    for frame, data in loc_keyframes_by_frame.items():
        keyframes.append({
            "bone_name": bone_name,
            "type": "location",
            "frame_index": frame,
            "data": data
        })

    for frame, data in rot_keyframes_by_frame.items():
        keyframes.append({
            "bone_name": bone_name,
            "type": "rotation_quaternion",
            "frame_index": frame,
            "data": data
        })

    if len(keyframes) == 0:
        print(f"No keyframes found for {bone_name}")
    return keyframes

def ExportAnimation(output_path, bl_rig_obj, reg_rig, rig_path):

    bl_rig = SkelRig()
    ensure_bl_mode_on_obj('EDIT', bl_rig_obj)
    bl_rig.from_blender(bl_rig_obj)

    ensure_bl_mode_on_obj('POSE', bl_rig_obj)
    animScene = AnimScene()
    animScene.LoadAnimationAttributes(bl_rig_obj)
    animScene.AddNewAnimationFromBlender(bl_rig_obj)
    animScene.correct_with_registered_rig(bl_rig, reg_rig)

    reg_rig_ptr = _LoadSFBGSSkeletonRigFromFileC(rig_path)
    animScenePtr = animScene.GetAnimationPtr(bl_rig, reg_rig_ptr,0)

    print(_SaveAnimationToSFBGSFormatWithExistingRigDirectC(
        animScenePtr,
        output_path,
        rig_path,
    ))
    ensure_object_mode()

def ImportAnimation(rig_path, input_path):
    rig_ptr = _LoadSFBGSSkeletonRigFromFileC(rig_path)
    rig = SkelRig()
    rig.from_ptr(rig_ptr, rig_path)

    animScene = AnimScene()
    animScene.ConstructFromFile(input_path, rig_path)
    return animScene

def ImportRig(rig_path):
    rig_ptr = _LoadSFBGSSkeletonRigFromFileC(rig_path)
    rig = SkelRig()
    rig.from_ptr(rig_ptr, rig_path)

    return rig

def ExportRig(obj, output_rig_path):
    rig = SkelRig()
    rig.from_blender(obj)
    rig_ptr = rig.to_ptr()
    _SaveSkeletonRigToSFBGSFormatDirectC(
        rig_ptr,
        ctypes.c_wchar_p(output_rig_path)
    )
