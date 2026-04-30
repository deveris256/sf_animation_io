import os

import mathutils

from API.AnimConverterFunc import (
    _GetSkeletonRigBoneCountC, _SFBGSRigPackage_GetPrecisionTypeC
)
from API import AnimationUtils
from API.AnimationBone import AnimBoneData
from API.RigBone import RigBone

flip_x = mathutils.Matrix.Scale(-1, 4, (0, 1, 0))
sca = mathutils.Matrix.Scale(1.000, 4, [1.0, 1.0, 1.0])

already_processed = []


class SkelRig():
    VALID_PRECISION = {
        0: "DEFAULT",
        1: "FIRST_PERSON",
        2: "SHIP",
        # TODO custom is unsupported at the moment
    }

    def __init__(self):
        self.name = "UNKNOWN RIG NAME"
        self.bones = []
        self._precision = "DEFAULT"

    @property
    def precision(self):
        # Stores int
        return self._precision

    @precision.setter
    def precision(self, value):
        try:
            if int(value) in list(SkelRig.VALID_PRECISION.keys()):
                self._precision = value
                return
        except:
            pass

        if value in list(SkelRig.VALID_PRECISION.values()):
            self._precision = list(SkelRig.VALID_PRECISION.keys())[list(SkelRig.VALID_PRECISION.values()).index(value)]
            return

        raise TypeError(
            f"Invalid precision specified: \'{value}\'")

    def LoadFromRigPtr(self, rig_ptr, rig_path):
        self.name = os.path.basename(rig_path).rpartition(".")[0]
        bone_count = _GetSkeletonRigBoneCountC(rig_ptr)
        self.precision = _SFBGSRigPackage_GetPrecisionTypeC(rig_ptr)

        for b_idx in range(bone_count):
            bone = RigBone()
            bone.LoadBoneFromRig(rig_ptr, b_idx)

            self.bones.append(bone)

    def SetArmatureAttributes(self, armature):
        armature.sf_rig_props.is_rig = True
        armature.sf_rig_props.rig_name = self.name
        armature.sf_rig_props.rig_precision = SkelRig.VALID_PRECISION[self.precision]

    def LoadArmatureAttributes(self, armature):
        self.name = armature.sf_rig_props.rig_name
        self.precision = armature.sf_rig_props.rig_precision

    def GetBoneByIndex(self, idx):
        match = [b for b in self.bones if b.index == idx]
        if len(match) >= 1:
            return match[0]
        return None

    def GetBone(self, bone_name):
        match = [b for b in self.bones if b.bone_name == bone_name]
        if len(match) >= 1:
            return match[0]
        return None

    def LoadFromArmature(self, armature_obj):
        self.LoadArmatureAttributes(armature_obj)

        bones = [b for b in armature_obj.data.edit_bones]
        bones = sorted(bones, key=lambda x: x.sf_bone_props.index)

        for b in bones:
            bone = RigBone()
            bone.LoadBoneFromArmature(armature_obj.data.edit_bones.get(b.name))
            self.bones.append(bone)

        # Post-process

        RevertRigCorrectBones(self.bones, armature_obj, [self.bones[0]])

def RevertRigCorrectBones(rig_bones, armature_obj, bones, parent_world_mat=None):
    if not bones:
        return

    for rig_bone in bones:
        bone = armature_obj.data.bones.get(rig_bone.bone_name)
        world_mat = bone.matrix_local.copy()
        world_mat = (
                world_mat @
                AnimationUtils.bone_axis_correction_full
        )

        world_mat = (
                AnimationUtils.bone_axis_correction_full @
                world_mat @
                AnimationUtils.bone_axis_correction_inv
        )
        if parent_world_mat is not None:
            local_mat = parent_world_mat.inverted() @ world_mat
        else:
            local_mat = world_mat

        loc, rot, sca = local_mat.decompose()

        rot = rot.normalized()

        rig_bone.translation = loc
        rig_bone.rotation.x = rot.x
        rig_bone.rotation.y = rot.y
        rig_bone.rotation.z = rot.z
        rig_bone.rotation.w = rot.w

        next_bones = [b for b in rig_bones if b.parent_name == rig_bone.bone_name]

        if len(next_bones) == 0:
            continue

        RevertRigCorrectBones(
            rig_bones,
            armature_obj,
            next_bones,
            world_mat
        )


class AnimFrameData():
    def __init__(self):
        self.bone_data = []

    def GetBoneDataByName(self, bone_name):
        for bdata in self.bone_data:
            if bdata.bone_name == bone_name:
                return self.bone_data.index(bdata)
        return None

    def AddGetBoneIndexBoneName(self, bone_name):
        b = self.GetBoneDataByName(bone_name)
        if b != None:
            return b

        anim_bone = AnimBoneData()
        anim_bone.bone_name = bone_name

        self.bone_data.append(anim_bone)

        return self.bone_data.index(self.bone_data[-1])


