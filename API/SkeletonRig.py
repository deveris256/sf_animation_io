import ctypes
import os
import bpy

from API import AnimationUtils
from API.RigBone import RigBone
from API.AnimConverterFunc import (
    _GetSkeletonRigBoneCountC, _CreateSkeletonRigC, _GetSkeletonBoneC, _GetSkeletonBoneChildC,
)

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
        self._precision = 0

    @property
    def precision(self):
        # Stores int
        return self._precision

    @precision.setter
    def precision(self, value):
        precision_ints = list(SkelRig.VALID_PRECISION.keys())
        precision_strs = list(SkelRig.VALID_PRECISION.values())

        if isinstance(value, str):
            if value.isdigit() and int(value) in list(precision_ints):
                self._precision = int(value)
            else:
                self._precision = precision_ints[precision_strs.index(value)]
        elif value in precision_ints:
            self._precision = value
        else:
            raise TypeError(f"Invalid precision specified: \'{value}\'")

    def from_ptr(self, rig_ptr, rig_path : str):
        """
        Loads rig from pointer
        """
        #print(rig_ptr)
        self.name = os.path.basename(rig_path).rpartition(".")[0]
        bone_count = _GetSkeletonRigBoneCountC(rig_ptr)

        #self.precision = _SFBGSRigPackage_GetPrecisionTypeC(rig_ptr)
        print(bone_count)

        root_bone_ptr = _GetSkeletonBoneC(rig_ptr, "Root".encode('utf-8'))
        root_bone = RigBone()
        root_bone.from_ptr(root_bone_ptr, None)
        self.bones.append(root_bone)

        self.bones_from_ptr_recursive(rig_ptr, bone_count, "Root", root_bone_ptr)

    def bones_from_ptr_recursive(self, rig_ptr, bone_count, parent_bone_name, parent_bone):
        for child_idx in range(bone_count):
            child_ptr = _GetSkeletonBoneChildC(parent_bone, child_idx)
            if child_ptr is None: break

            bone = RigBone()
            bone.from_ptr(child_ptr, parent_bone_name)
            print("FROM PTR", bone.bone_name, parent_bone_name)

            self.bones.append(bone)
            self.bones_from_ptr_recursive(rig_ptr, bone_count, bone.bone_name, child_ptr)

    def set_blender_armature_attr(self, armature : bpy.types.Object):
        """Sets Blender armature attributes"""
        armature.sf_rig_props.is_rig = True
        armature.sf_rig_props.rig_name = self.name
        armature.sf_rig_props.rig_precision = SkelRig.VALID_PRECISION[self.precision]

    def load_blender_armature_attr(self, armature : bpy.types.Object):
        """Loads Blender armature attributes"""
        self.name = armature.sf_rig_props.rig_name
        self.precision = armature.sf_rig_props.rig_precision

    def get_bone_by_index(self, idx : int):
        """Gets bone by index"""
        match = [b for b in self.bones if b.index == idx]
        if len(match) >= 1:
            return match[0]
        return None

    def get_bone_by_name(self, bone_name : str):
        """Gets bone by name"""
        match = [b for b in self.bones if b.bone_name == bone_name]
        if len(match) >= 1:
            return match[0]
        return None

    def from_blender(self, armature_obj : bpy.types.Object):
        """
        Loads data from armature
        """
        self.load_blender_armature_attr(armature_obj)

        if len(armature_obj.data.edit_bones) == 0:
            raise Exception("Zero bones found")

        for b in armature_obj.data.edit_bones:
            bone = RigBone()
            bone.from_blender(b)
            self.bones.append(bone)

        # Post-process
        #revert_rig_bone_correction(self.bones, armature_obj, [self.bones[0]])

    def to_ptr(self):
        """Returns a rig pointer"""
        #cont = _CreateStringContainerC()
        rig_ptr = _CreateSkeletonRigC(self.name.encode('utf-8'))
        #_SFBGSRigPackage_AddPackageToSkeletonRigC(rig_ptr, cont, ctypes.c_bool(True))

        for idx, bone in enumerate(self.bones):
            bone.to_ptr(rig_ptr, idx)

        return rig_ptr
