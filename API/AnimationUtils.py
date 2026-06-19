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

        SetAnimationBoneMatrix(frame_bone, pose_bone, frame_num)

def SetAnimationBoneMatrix(frame_bone, pose_bone, frame_num):
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

    mat = t @ r @ s # animation-delta matrix (without premultiplied armature bone data)
    mat = mat

    local_bone_mat = pose_bone.bone.matrix.to_4x4() # local bone matrix in armature space
    local_bone_mat_uncorr = inv_correct_bone_axis(local_bone_mat) # uncorrected

    local_bone_mat_infl = local_bone_mat_uncorr @ mat # influenced with anim
    local_bone_mat_infl_corr = bone_axis_correction_full @ local_bone_mat_infl @ bone_axis_correction_inv # influenced and corrected
    local_bone_mat_delta = local_bone_mat.inverted() @ local_bone_mat_infl_corr # delta (bone mat vs anim bone corr)
    local_bone_mat_delta = local_bone_mat_delta

    pose_bone.matrix_basis = local_bone_mat_delta

    if scale:
        pose_bone.keyframe_insert(data_path='scale', frame=frame_num)

    if translate:
        pose_bone.keyframe_insert(data_path='location', frame=frame_num)

    if rotate:
        pose_bone.keyframe_insert(data_path='rotation_quaternion', frame=frame_num)
