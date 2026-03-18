import ctypes

from API.AnimConverterFunc import (
    _LoadSFBGSSkeletonRigFromFileC, _SaveAnimationToSFBGSFormatWithExistingRigDirectC,
    _CreateSkeletonRigC, _AddBoneToSkeletonRigC, _GetSkeletonBoneC,
    _SetBoneTypeC, _SetTwistBonePropertiesC, _SetMirrorIndexC, _SaveSkeletonRigToSFBGSFormatDirectC,
    _CreateStringContainerC, _GetStringFromContainerC, _SFBGSRigPackage_AddBoneNameToMapC,
    _SFBGSRigPackage_AddPackageToSkeletonRigC
)
from API.AnimationIOWrappers import SkelRig
from API.Animation import AnimData
from API.AnimationScene import AnimScene


def LoadRigPtr(rig_path):
    err = ctypes.c_char()
    print("Rig path:", rig_path)
    rigPtr = _LoadSFBGSSkeletonRigFromFileC(
        ctypes.c_wchar_p(rig_path),
        ctypes.c_bool(False)
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

def ExportAnimation(output_path, rig_obj, rig_path):
    rigData = SkelRig()
    rig_ptr = LoadRigPtr(rig_path)
    rigData.LoadFromRigPtr(rig_ptr, rig_path)

    animScene = AnimScene()
    animScene.LoadAnimationAttributes(rig_obj)
    animScene.AddNewAnimationFromBlender(rig_obj, rigData)

    animScenePtr = animScene.GetAnimationPtr(rigData, rig_path, 0)

    print(_SaveAnimationToSFBGSFormatWithExistingRigDirectC(
        animScenePtr,
        output_path,
        rig_path,
        ctypes.c_bool(False)
    ))

def ImportAnimation(rig_path, input_path):
    animScene = AnimScene()
    animScene.ConstructFromFile(input_path, rig_path)
    return animScene

def ImportRig(rig_path):
    rig_ptr = _LoadSFBGSSkeletonRigFromFileC(rig_path, ctypes.c_bool(False))
    rig = SkelRig()
    rig.LoadFromRigPtr(rig_ptr, rig_path)

    return rig

def ExportRig(obj, output_rig_path):
    rig = SkelRig()
    rig.LoadFromArmature(obj)

    cont = _CreateStringContainerC()

    rig_ptr = _CreateSkeletonRigC(rig.name.encode('utf-8'))
    _SFBGSRigPackage_AddPackageToSkeletonRigC(rig_ptr, cont, ctypes.c_bool(True))

    for idx, bone in enumerate(rig.bones):
        _AddBoneToSkeletonRigC(
            rig_ptr,
            bone.rotation.x,
            bone.rotation.y,
            bone.rotation.z,
            bone.rotation.w,

            bone.translation[0], # x
            bone.translation[1], # y
            bone.translation[2], # z

            bone.bone_name.encode('utf-8'),

            bone.parent_index if bone.parent_index is not None else -1,

            ctypes.c_bool(True),

            cont
        )

        bone_ptr = _GetSkeletonBoneC(rig_ptr, idx, ctypes.c_bool(False))

        if bone.mapping != 255:
            if _SFBGSRigPackage_AddBoneNameToMapC(
                rig_ptr,
                bone.mapping,
                bone.bone_name.encode('utf-8'),
                cont,
                ctypes.c_bool(False)
            ) == False:
                print((
                    rig_ptr,
                    bone.mapping,
                    bone.bone_name.encode('utf-8'),
                    cont,
                    ctypes.c_bool(False)
                ))
                raise Exception(_GetStringFromContainerC(cont).decode('utf-8'))

        _SetBoneTypeC(bone_ptr, bone.bone_type)
        _SetMirrorIndexC(bone_ptr, bone.mirror_index)

        if bone.bone_type_blender == "Twist":
            _SetTwistBonePropertiesC(bone_ptr, ctypes.c_bool(True),
                                     bone.twist_bone_driver_index, bone.twist_bone_driver_weight, cont)

    print(output_rig_path)
    print(_SaveSkeletonRigToSFBGSFormatDirectC(
        rig_ptr,
        ctypes.c_wchar_p(output_rig_path),
        cont
    ))

    print(_GetStringFromContainerC(cont).decode('utf-8'))
