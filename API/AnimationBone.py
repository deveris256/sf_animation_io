import ctypes

import mathutils

from API.AnimConverterFunc import (
    _GetValueFromScalarFrameC, _GetValueFromRotationFrameC, _GetQuaternionXC, _GetQuaternionYC, _GetQuaternionZC,
    _GetQuaternionWC, _GetValueFromTranslationFrameC, _GetVector3DXC, _GetVector3DYC, _GetVector3DZC,
    _CreateScalarFrameC, _AddScalarSqToAnimBlockC, _AddTranslationSqToAnimBlockC, _CreateTranslationFrameC,
    _CreateRotationFrameC, _AddRotationSqToAnimBlockC,
)

class AnimationBoneScale:
    """
    Wrapper class for handling animation
    bone scale.
    """
    def __init__(self, raw_scale=None):
        self.raw_scale = raw_scale

    @property
    def is_none(self):
        return True if self.raw_scale is None else False

    @property
    def raw(self):
        return self.raw_scale

    @raw.setter
    def raw(self, value):
        self.raw_scale = value

    @property
    def blender(self) -> tuple:
        return self.raw_scale, self.raw_scale, self.raw_scale

    @blender.setter
    def blender(self, value):
        """Expects iterable"""
        self.raw_scale = max(value)

    def PtrSetScale(self, sqs):
        sqs_uniform = _GetValueFromScalarFrameC(sqs)
        self.raw = sqs_uniform

class AnimationBoneRotation:
    """
    Wrapper class for handling animation
    bone rotation between blender and dll,
    with conversion methods.
    """

    def __init__(self, raw_rotation=None):
        if raw_rotation is not None:
            self.x = raw_rotation[0]
            self.y = raw_rotation[1]
            self.z = raw_rotation[2]
            self.w = raw_rotation[3]
        else:
            self.x = None
            self.y = None
            self.z = None
            self.w = None

    @property
    def is_none(self):
        return all([True if r is None else False for r in [self.x, self.y, self.z, self.w]])

    @property
    def raw_xyzw(self):
        return self.x, self.y, self.z, self.w

    @raw_xyzw.setter
    def raw_xyzw(self, value):
        self.x = value[0]
        self.y = value[1]
        self.z = value[2]
        self.w = value[3]

    @property
    def raw_wxyz(self):
        return self.w, self.x, self.y, self.z

    @raw_wxyz.setter
    def raw_wxyz(self, value):
        self.w = value[0]
        self.x = value[1]
        self.y = value[2]
        self.z = value[3]
        raise Exception(len(value))

    def get_blender_compatible_euler(self):
        """""" # TODO

    def PtrSetRotation(self, rsq):
        quat = _GetValueFromRotationFrameC(rsq)

        r_x = _GetQuaternionXC(quat)
        r_y = _GetQuaternionYC(quat)
        r_z = _GetQuaternionZC(quat)
        r_w = _GetQuaternionWC(quat)

        self.raw_xyzw = (r_x, r_y, r_z, r_w)

class AnimationBoneTranslation:
    """
    Wrapper class for Anim Bone translation with nice handling of
    raw and Blender-ready values.
    """

    def __init__(self):
        self.x = None
        self.y = None
        self.z = None

    @property
    def is_none(self):
        return all([True if r is None else False for r in [self.x, self.y, self.z]])

    @property
    def raw(self):
        return self.x, self.y, self.z

    @raw.setter
    def raw(self, value):
        self.x = value[0]
        self.y = value[1]
        self.z = value[2]

    @property
    def blender(self):
        x = self.x
        y = self.y
        z = self.z
        return x, y, z

    @blender.setter
    def blender(self, value):
        self.x = value[0]
        self.y = value[1]
        self.z = value[2]
        raise

    def PtrSetTranslation(self, tsq):
        vec = _GetValueFromTranslationFrameC(tsq)

        t_x = _GetVector3DXC(vec)
        t_y = _GetVector3DYC(vec)
        t_z = _GetVector3DZC(vec)

        self.raw = (t_x, t_y, t_z)


class AnimBoneData:
    """
    Wrapper class for handling animation
    bone data.
    """
    def __init__(self):
        self.translation = AnimationBoneTranslation()
        self.rotation = AnimationBoneRotation()
        self.scale = AnimationBoneScale()
        self.bone_name = None
        self.index = None

    def get_matrix(self):
        if self.translation.is_none:
            tra = mathutils.Matrix.Translation((0.0, 0.0, 0.0))
        else:
            tra = mathutils.Matrix.Translation(self.translation.blender)
        if self.rotation.is_none:
            rot = mathutils.Matrix.Rotation(0, 4, (0,0,0))
        else:
            rot = mathutils.Quaternion(self.rotation.raw_wxyz).to_matrix().to_4x4()

        if self.scale.is_none:
            sca = mathutils.Matrix.Scale(1.0, 4, (1.0, 1.0, 1.0))
        else:
            sca = mathutils.Matrix.Scale(1.000, 4, self.scale.blender)
        return tra @ rot @ sca

    def set_from_matrix(self, matrix):
        tra, rot, sca = matrix.decompose()
        self.translation.blender = tra
        self.rotation.raw_wxyz = rot
        self.scale.blender = sca

    def load_from_blender(self, pose_bone, armature):
        M = armature.convert_space(
            pose_bone=pose_bone,
            matrix=pose_bone.matrix,
            from_space='POSE',
            to_space='LOCAL',
        ).decompose()

        translation = M[0]
        rotation = M[1]
        scale = M[2]

        self.translation.blender = translation
        self.rotation.raw_wxyz = rotation.wxyz
        self.scale.blender = scale

    def AddDataToBlockPtr(self, frame_idx, anim_block_ptr):
        # SQS
        block_has_data = False
        if not self.scale.is_none:
            block_has_data = True
            sqs_entry_float = self.scale.raw
            sqs = _CreateScalarFrameC(
                frame_idx,
                sqs_entry_float
            )

            _AddScalarSqToAnimBlockC(
                anim_block_ptr, sqs, 1, ctypes.c_bool(True))

        # TSQ
        if not self.translation.is_none:
            block_has_data = True
            tsq_entry_tuple = self.translation.raw
            tsq = _CreateTranslationFrameC(
                frame_idx,
                tsq_entry_tuple[0],
                tsq_entry_tuple[1],
                tsq_entry_tuple[2])

            _AddTranslationSqToAnimBlockC(
                anim_block_ptr, tsq, 1, ctypes.c_bool(True))

        # RSQ
        if not self.rotation.is_none:
            block_has_data = True
            rsq_entry_tuple = self.rotation.raw_xyzw

            rsq = _CreateRotationFrameC(
                frame_idx,
                rsq_entry_tuple[0], rsq_entry_tuple[1],
                rsq_entry_tuple[2], rsq_entry_tuple[3])

            _AddRotationSqToAnimBlockC(
                anim_block_ptr,
                rsq,
                1, ctypes.c_bool(True)
            )

        return block_has_data
