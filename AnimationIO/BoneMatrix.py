from mathutils import Matrix
import math
from math import radians
from bpy_extras.io_utils import axis_conversion

bone_axis_correction_180 = Matrix.Rotation(radians(180.0), 4, 'Z')
bone_axis_correction_m180 = Matrix.Rotation(radians(-180.0), 4, 'Z')

bone_axis_correction_90 = Matrix.Rotation(radians(90.0), 4, 'Z')
bone_axis_correction_m90 = Matrix.Rotation(radians(-90.0), 4, 'Z')

corr_matrix = axis_conversion(from_forward='Y', from_up='Z', to_forward='-Y', to_up='Z').to_4x4()

def matrix_construct_helper(value):
    """
    Helps to construct 4x4 matrix
    from either:
    tuple of (tra,rot,sca),
    tuple of (tra,rot)
    any other matrix
    """
    if isinstance(value, Matrix):
        mat = value.to_4x4()
    elif isinstance(value, tuple): # assumes tuple of (vector, quaternion, optional scale)
        tra = Matrix.Translation(value[0])
        rot = value[1].to_matrix().to_4x4()
        sca = Matrix.Scale(1.0, 4) if len(value) == 2 else value[2]
        mat = tra @ rot @ sca
    else:
        raise Exception("Attempted to set invalid world_bone_matrix value")
    return mat

class BoneMatrix:
    """
    Overlay matrix should be bone-relative.
    """
    def __init__(self):
        self._world_bone_matrix = Matrix.Identity(4)
        self._overlay_matrices = {}
        self._overlay_matrices_mask = {} # tra, rot, sca

    def __repr__(self):
        return f"BoneMatrix\n{self._world_bone_matrix}"

    def clear_overlay_matrix(self):
        self._overlay_matrices_mask = {}
        self._overlay_matrices = {}

    def set_overlay_matrix(self, frame_id, overlay_matrix, mask):
        frame_id = int(frame_id)
        overlay_mat = matrix_construct_helper(overlay_matrix)
        self._overlay_matrices[frame_id] = overlay_mat
        self._overlay_matrices_mask[frame_id] = mask

    def set_overlay_matrix_from_blender(self, frame_id, overlay_matrix, mask):
        frame_id = int(frame_id)
        overlay_mat = matrix_construct_helper(overlay_matrix)
        self._overlay_matrices[frame_id] = bone_axis_correction_m90.to_4x4() @ overlay_mat @ bone_axis_correction_90.to_4x4()
        self._overlay_matrices_mask[frame_id] = mask

    def get_overlay_matrix_or_identity(self, frame_id):
        frame_id = int(frame_id)
        if frame_id in self._overlay_matrices.keys():
            return True, self._overlay_matrices[frame_id]
        return False, Matrix.Identity(4)

    def get_blender_compatible_overlay_matrix(self, frame_id):
        frame_id = int(frame_id)
        if frame_id in self._overlay_matrices.keys():
            base_overlay_mat = self._overlay_matrices[frame_id]
            out_mat = bone_axis_correction_90.to_4x4() @ base_overlay_mat @ bone_axis_correction_m90.to_4x4()
            return True, out_mat
        return False, Matrix.Identity(4)

    @property
    def world_bone_matrix(self):
        return self._world_bone_matrix

    @world_bone_matrix.setter
    def world_bone_matrix(self, value):
        self._world_bone_matrix = matrix_construct_helper(value)

    @property
    def blender_compatible_bone_world_matrix(self):
        test = bone_axis_correction_180 @ self._world_bone_matrix @ bone_axis_correction_m90
        return test

    @blender_compatible_bone_world_matrix.setter
    def blender_compatible_bone_world_matrix(self, value):
        self._world_bone_matrix = bone_axis_correction_m180 @ value @ bone_axis_correction_90


