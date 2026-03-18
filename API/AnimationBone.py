import ctypes

import mathutils

from API.AnimConverterFunc import _CreateScalarEntryC, _AddScalarSqToAnimBlockC, _CreateTranslationEntryC, \
    _AddTranslationSqToAnimBlockC, _CreateRotationEntryC, _AddRotationSqToAnimBlockC, _GetTranslationSqSizeC, \
    _GetTranslationFromSqC, _GetVector3DX, _GetVector3DZ, _GetVector3DY, _GetValueFromTranslationEntryC, \
    _GetValueFromScalarEntryC, _GetValueFromRotationEntryC, _GetQuaternionX, _GetQuaternionY, _GetQuaternionW, \
    _GetQuaternionZ
from API.AnimationUtils import BoneAxisCorrection, BoneAxisCorrectionInv

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
        sqs_uniform = _GetValueFromScalarEntryC(sqs)
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

    @property
    def blender_quaternion(self):
        return AnimationBoneRotation.RsqRotationToBlenderQuaternion(self.raw_wxyz)

    @blender_quaternion.setter
    def blender_quaternion(self, value):
        quat = AnimationBoneRotation.BlenderQuaternionToRsqRotation(value)
        self.x = quat.x
        self.y = quat.y
        self.z = quat.z
        self.w = quat.w

    @property
    def blender_euler(self):
        rot = self.blender_quaternion.to_euler()
        return rot.x, rot.y, rot.z

    def RsqRotationToBlenderQuaternion(raw_quaternion: tuple[float, float, float, float]):
        R_src = mathutils.Quaternion(raw_quaternion).to_matrix().to_4x4()
        R_bpy = BoneAxisCorrection(R_src)
        return R_bpy.to_quaternion()

    def BlenderQuaternionToRsqRotation(blender_quaternion: mathutils.Quaternion):
        R_src = blender_quaternion.to_matrix().to_4x4()
        R_raw = BoneAxisCorrectionInv(R_src)
        return R_raw.to_quaternion()

    def PtrSetRotation(self, rsq):
        quat = _GetValueFromRotationEntryC(rsq)

        r_x = _GetQuaternionX(quat)
        r_y = _GetQuaternionY(quat)
        r_z = _GetQuaternionZ(quat)
        r_w = _GetQuaternionW(quat)

        self.raw_xyzw = (r_x, r_y, r_z, r_w)

class AnimationBoneTranslation:
    """
    Wrapper class for Anim Bone translation with nice handling of
    raw and Blender-ready values.
    """

    def __init__(self, raw_translation=None):
        if raw_translation is not None:
            self.x = raw_translation[0]
            self.y = raw_translation[1]
            self.z = raw_translation[2]
        else:
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
        x = -self.z  # -Z to X
        y = self.x  # X to Y
        z = self.y  # Y to Z
        return x, y, z

    @blender.setter
    def blender(self, value):
        if value[1] is not None: self.x = value[1]
        if value[2] is not None: self.z = value[2]
        if value[0] is not None: self.y = -value[0]

    def PtrSetTranslation(self, tsq):
        vec = _GetValueFromTranslationEntryC(tsq)

        t_x = _GetVector3DX(vec)
        t_y = _GetVector3DZ(vec)
        t_z = _GetVector3DY(vec)

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

    def AddDataToBlockPtr(self, frame_idx, anim_block_ptr):
        # SQS
        block_has_data = False
        if not self.scale.is_none:
            block_has_data = True
            sqs_entry_float = self.scale.raw
            sqs = _CreateScalarEntryC(
                frame_idx,
                sqs_entry_float
            )

            _AddScalarSqToAnimBlockC(
                anim_block_ptr, sqs, 1, ctypes.c_bool(True))

        # TSQ
        if not self.translation.is_none:
            block_has_data = True
            tsq_entry_tuple = self.translation.raw
            tsq = _CreateTranslationEntryC(
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

            rsq = _CreateRotationEntryC(
                frame_idx,
                rsq_entry_tuple[0], rsq_entry_tuple[1],
                rsq_entry_tuple[2], rsq_entry_tuple[3])

            _AddRotationSqToAnimBlockC(
                anim_block_ptr,
                rsq,
                1, ctypes.c_bool(True)
            )

        return block_has_data
