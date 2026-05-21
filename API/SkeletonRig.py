import ctypes
import os

from API import AnimationUtils
from API.AnimConverterFunc import _GetSkeletonRigBoneCountC, _SFBGSRigPackage_GetPrecisionTypeC, _CreateSkeletonRigC, \
    _SFBGSRigPackage_AddPackageToSkeletonRigC, _CreateStringContainerC, _AddBoneToSkeletonRigC
from API.RigBone import RigBone


class SkelRig:
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

    @precision.setter # todo, it looks like it causes problems.
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
        """
        Loads rig from pointer
        """
        self.name = os.path.basename(rig_path).rpartition(".")[0]
        bone_count = _GetSkeletonRigBoneCountC(rig_ptr)
        self.precision = _SFBGSRigPackage_GetPrecisionTypeC(rig_ptr)

        for b_idx in range(bone_count):
            bone = RigBone()
            bone.from_ptr(rig_ptr, b_idx)

            self.bones.append(bone)

    def SetArmatureAttributes(self, armature):
        """
        Sets Blender armature attributes
        """
        armature.sf_rig_props.is_rig = True
        armature.sf_rig_props.rig_name = self.name
        armature.sf_rig_props.rig_precision = SkelRig.VALID_PRECISION[self.precision]

    def LoadArmatureAttributes(self, armature):
        """
        Loads data from Blender armature attributes
        """
        self.name = armature.sf_rig_props.rig_name
        self.precision = armature.sf_rig_props.rig_precision

    def GetBoneByIndex(self, idx):
        """
        Gets bone by index
        """
        match = [b for b in self.bones if b.index == idx]
        if len(match) >= 1:
            return match[0]
        return None

    def GetBone(self, bone_name):
        """
        Gets bone by name
        """
        match = [b for b in self.bones if b.bone_name == bone_name]
        if len(match) >= 1:
            return match[0]
        return None

    def LoadFromArmature(self, armature_obj):
        """
        Loads data from armature
        """
        self.LoadArmatureAttributes(armature_obj)

        bones = [b for b in armature_obj.data.edit_bones]
        bones = sorted(bones, key=lambda x: x.sf_bone_props.index)

        for b in bones:
            bone = RigBone()
            bone.from_blender(armature_obj.data.edit_bones.get(b.name))
            self.bones.append(bone)

        # Post-process
        RevertRigCorrectBones(self.bones, armature_obj, [self.bones[0]])

    def to_ptr(self):
        """Returns a rig pointer"""
        cont = _CreateStringContainerC()
        rig_ptr = _CreateSkeletonRigC(self.name.encode('utf-8'))
        _SFBGSRigPackage_AddPackageToSkeletonRigC(rig_ptr, cont, ctypes.c_bool(True))

        for idx, bone in enumerate(self.bones):
            bone.to_ptr(rig_ptr, idx)

def RevertRigCorrectBones(rig_bones, armature_obj, bones, parent_world_mat=None):
    """
    Recursively reverts rig bone corrections,
    which were applied on rig import.
    """
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
