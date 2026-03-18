import math
import mathutils

bone_axis_correction = mathutils.Matrix.Rotation(math.radians(90.0), 4, 'Z')
bone_axis_correction_inv = mathutils.Matrix.Rotation(math.radians(-90.0), 4, 'Z')

bone_axis_correction_full = mathutils.Matrix.Rotation(math.radians(180.0), 4, 'Z')
bone_axis_correction_full_inv = mathutils.Matrix.Rotation(math.radians(-180.0), 4, 'Z')

def BoneAxisCorrection(T):
    return bone_axis_correction @ T @ bone_axis_correction_inv

def BoneAxisCorrectionInv(T):
    return bone_axis_correction_inv @ T @ bone_axis_correction

def BoneAxisCorrection_Alt(T):
    return (bone_axis_correction_full @ T @ bone_axis_correction_inv)

def LoadAnim(armature_obj, frame_num, frame_bones_list):
    pose_bones = armature_obj.pose.bones

    for frame_bone in frame_bones_list:
        if pose_bones.get(frame_bone.bone_name) == None:
            raise Exception((f"No pose-bone found", frame_bone.bone_name))
        else:
            pose_bone = pose_bones.get(frame_bone.bone_name)

        SetAnimationBoneMatrix(frame_bone, pose_bone, frame_num)

def SetAnimationBoneMatrix(frame_bone, pose_bone, frame_num):
    pose_bone.rotation_mode = 'QUATERNION'

    if not frame_bone.scale.is_none:
        pose_bone.scale = frame_bone.scale.blender
        pose_bone.keyframe_insert(data_path='scale', frame=frame_num)
    if not frame_bone.translation.is_none:
        pose_bone.location = frame_bone.translation.blender
        pose_bone.keyframe_insert(data_path='location', frame=frame_num)
    if not frame_bone.rotation.is_none:
        pose_bone.rotation_quaternion = frame_bone.rotation.blender_quaternion
        pose_bone.keyframe_insert(data_path='rotation_quaternion', frame=frame_num)
        temp = frame_bone.rotation.blender_quaternion.to_euler()
        print(math.degrees(temp.x), math.degrees(temp.y), math.degrees(temp.z))
