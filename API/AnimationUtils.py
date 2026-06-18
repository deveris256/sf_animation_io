import math
import mathutils
from bpy_extras.io_utils import axis_conversion

from API.RigUtils import correct_bone_axis, inv_correct_bone_axis, bone_axis_correction_full, bone_axis_correction, \
    bone_axis_correction_inv, bone_axis_correction_full_inv


def LoadAnim(armature_obj, frame_num, frame_bones_list):
    pose_bones = armature_obj.pose.bones

    for frame_bone in frame_bones_list:
        if pose_bones.get(frame_bone.bone_name) == None:
            raise Exception((f"No pose-bone found", frame_bone.bone_name))
        else:
            pose_bone = pose_bones.get(frame_bone.bone_name)

        SetAnimationBoneMatrix(armature_obj, frame_bone, pose_bone, frame_num)

def SetAnimationBoneMatrix(armature, frame_bone, pose_bone, frame_num):
    pose_bone.rotation_mode = 'QUATERNION'

    rotate = False
    translate = False
    scale = False

    if frame_bone.scale.is_none:
        s = mathutils.Matrix.Identity(4)
    else:
        scale = True
        s = mathutils.Matrix.Scale(frame_bone.scale.raw, 4)

    if frame_bone.translation.is_none:
        t = mathutils.Matrix.Identity(4)
    else:
        translate = True
        t = mathutils.Matrix.Translation(frame_bone.translation.raw).to_4x4()

    if frame_bone.rotation.is_none:
        r = mathutils.Matrix.Identity(4)
    else:
        rotate = True
        r = mathutils.Quaternion(frame_bone.rotation.raw_wxyz).to_matrix().to_4x4()

    print(t.translation)
    print(r.to_euler())
    print(s)

    r = r.to_euler()
    r_temp = r.copy()

    r.x = -r_temp.y
    r.y = -r_temp.x
    r.z = -r_temp.z

    r = r.to_matrix().to_4x4()


    mat = t @ r @ s
    #mat = armature.convert_space(
    #    pose_bone=pose_bone,
    #    matrix=mat,
    #    from_space="POSE",
    #    to_space="LOCAL"
    #).to_3x3()
   # mat = mat.to_3x3()
    # Y = up

    #mat = mat @ mathutils.Matrix.Rotation(math.radians(-180), 3, 'Y')
    #mat = mathutils.Matrix.Rotation(math.radians(-90), 4, 'Y') @ mat
    #mat = mathutils.Matrix.Rotation(math.radians(90), 4, 'Z') @ mat
    #mat = mathutils.Matrix.Rotation(math.radians(-90), 4, 'X') @ mat
    #mat.rotate(mathutils.Matrix.Rotation(math.radians(180), 3, 'Y'))
    #mat.rotate(mathutils.Matrix.Rotation(math.radians(-90), 3, 'Y'))
    #mat = mat.to_4x4() @ bone_axis_correction_full_inv
    #.rotate(mathutils.Matrix.Rotation(math.radians(180), 3, 'Y'))
    #mat.rotate(mathutils.Matrix.Rotation(math.radians(-90), 3, 'X'))
    #mat = correct_bone_axis(mat.to_4x4()).to_3x3()
    #mat.rotate(mathutils.Matrix.Rotation(math.radians(90), 3, 'X'))
    #mat.rotate(mathutils.Matrix.Rotation(math.radians(-90.0), 3, 'Y'))
    #mat.rotate(mathutils.Matrix.Rotation(math.radians(180.0), 3, 'Z'))
    #mat = mat.to_4x4()
    #mat = armature.convert_space(
    #    pose_bone=pose_bone,
    #    matrix=mat,
    #    from_space="LOCAL",
    #    to_space="POSE"
    #)

    #mat = armature.convert_space(
    #    pose_bone=pose_bone,
    #    matrix=mat,
    #    from_space="WORLD",
    #    to_space="POSE"
    #)

    t, r, s = mat.decompose()

    if scale:
        pose_bone.scale = list(s.to_scale())
        pose_bone.keyframe_insert(data_path='scale', frame=frame_num)

    if translate:
        pose_bone.location = t
        pose_bone.keyframe_insert(data_path='location', frame=frame_num)

    if rotate:
        pose_bone.rotation_quaternion = r
        pose_bone.keyframe_insert(data_path='rotation_quaternion', frame=frame_num)
