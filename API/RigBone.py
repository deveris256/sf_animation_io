import ctypes

from API.AnimConverterFunc import _GetMirrorIndexC, _GetTwistBoneDriverIndexC, _GetTwistBoneDriverWeightC, \
    _GetBoneTypeC, _GetSkeletonBoneParentIndexC, _GetSkeletonBoneC, _GetSkeletonBoneNameC, _GetSkeletonBoneRotationC, \
    _GetQuaternionX, _GetQuaternionY, _GetQuaternionZ, _GetQuaternionW, _GetSkeletonBonePositionC, _GetVector3X, \
    _GetVector3Y, _GetVector3Z, _SFBGSRigPackage_BoneIsMappedC, _SFBGSRigPackage_GetBoneKeyC


class RigBone():
    """
    RigBone class stores data of a rig bone in an
    easily accessible to Python way.
    """

    bone_types = {
        0: "Default",
        1: "Twist",
    }

    bone_types_inv = {v: k for k, v in bone_types.items()}

    def __init__(self):
        self.bone_name = None
        self.rotation = RigBoneRotation()
        self.translation = None

        self.parent_name = None
        self.parent_index = None

        self.index = None

        self.rig_bone_index = None
        self.mirror_index = -1
        self.twist_bone_driver_index = -1
        self.twist_bone_driver_weight = None
        self._bone_type = 0
        self.mapping = int(0xFF)

    @property
    def bone_type_blender(self):
        return RigBone.bone_types[self._bone_type]

    @bone_type_blender.setter
    def bone_type_blender(self, value):
        val = value

        if isinstance(value, str):
            if val.isdigit():
                val = int(val)
            else:
                val = RigBone.bone_types_inv[val]
        elif not val in RigBone.bone_types.keys():
            raise Exception(f"Unable to set bone type to {val}")

        self._bone_type = val

    @property
    def bone_type(self):
        return self._bone_type

    @bone_type.setter
    def bone_type(self, value):
        val = value

        if isinstance(value, str):
            if val.isdigit():
                val = int(val)
            else:
                val = RigBone.bone_types_inv[val]
        elif not val in RigBone.bone_types.keys():
            raise Exception(f"Unable to set bone type to {val}")

        self._bone_type = val

    def SetArmatureBoneAttributes(self, armature_bone):
        """Sets Armature's bone attributes"""
        armature_bone.sf_bone_props.index = self.index
        armature_bone.sf_bone_props.mirror_index = self.mirror_index
        armature_bone.sf_bone_props.bone_type = str(self.bone_type_blender)
        armature_bone.sf_bone_props.twist_bone_driver_weight = self.twist_bone_driver_weight
        armature_bone.sf_bone_props.mapping = str(self.mapping)

        if RigBone.bone_types[self.bone_type] == "Twist":
            armature_bone.sf_bone_props.twist_bone_driver_index = self.twist_bone_driver_index
            armature_bone.sf_bone_props.twist_bone_driver_weight = self.twist_bone_driver_weight

    def LoadArmatureBoneAttributes(self, armature_bone):
        """Loads attributes from Armature's editbone"""
        self.index = armature_bone.sf_bone_props.index
        self.mirror_index = armature_bone.sf_bone_props.mirror_index
        self.bone_type_blender = armature_bone.sf_bone_props.bone_type
        self.mapping = int(armature_bone.sf_bone_props.mapping)

        if armature_bone.sf_bone_props.bone_type == "Twist":
            self.twist_bone_driver_index = armature_bone.sf_bone_props.twist_bone_driver_index
            self.twist_bone_driver_weight = armature_bone.sf_bone_props.twist_bone_driver_weight


    def PtrSetBoneAttributes(self, rig_bone):
        """
        Sets bone attributes
        """
        self.rig_bone_index = self.index # TODO TODO
        self.mirror_index = _GetMirrorIndexC(rig_bone)
        self.twist_bone_driver_index = _GetTwistBoneDriverIndexC(rig_bone, ctypes.c_bool(False))
        self.twist_bone_driver_weight = _GetTwistBoneDriverWeightC(rig_bone, ctypes.c_bool(False))
        self.bone_type = _GetBoneTypeC(rig_bone)

    def PtrSetBoneParent(self, rig_bone, rig_ptr):
        """
        Sets bone parent name and index
        from SkeletonRig*
        """
        err = ctypes.c_char()
        parent_index = _GetSkeletonBoneParentIndexC(rig_bone)

        if parent_index != -1:
            parent_bone = _GetSkeletonBoneC(
                rig_ptr,
                parent_index,
                ctypes.c_bool(False)
            )
            self.parent_name = _GetSkeletonBoneNameC(parent_bone).decode('utf-8').strip()
            self.parent_index = parent_index
        else:
            self.parent_name = None
            self.parent_index = -1

    def PtrSetBoneRotation(self, rig_bone):
        """
        Sets bone rotation from ptr
        """
        bone_r = _GetSkeletonBoneRotationC(rig_bone, False)

        try:
            self.rotation.x = _GetQuaternionX(bone_r)
            self.rotation.y = _GetQuaternionY(bone_r)
            self.rotation.z = _GetQuaternionZ(bone_r)
            self.rotation.w = _GetQuaternionW(bone_r)
        except Exception as e:
            self.rotation.x = 0.0
            self.rotation.y = 0.0
            self.rotation.z = 0.0
            self.rotation.w = 0.0

    def PtrSetBoneTranslation(self, rig_bone):
        """
        Sets bone translation from ptr
        """
        bone_t = _GetSkeletonBonePositionC(rig_bone, False)

        try:
            x = _GetVector3X(bone_t)
            y = _GetVector3Y(bone_t)
            z = _GetVector3Z(bone_t)
        except Exception as e:
            x = 0.0
            y = 0.0
            z = 0.0

        self.translation = (x, y, z)

    def PtrSetBoneMapping(self, rig_ptr):
        """
        Sets bone mapping from ptr
        """
        if _SFBGSRigPackage_BoneIsMappedC(rig_ptr, self.bone_name.encode('utf-8')):
            self.mapping = _SFBGSRigPackage_GetBoneKeyC(rig_ptr, self.bone_name.encode('utf-8'))

    def LoadBoneFromRig(self, rig_ptr, b_idx):
        """Loads bone from rig pointer"""
        rig_bone = _GetSkeletonBoneC(
            rig_ptr,
            b_idx,
            ctypes.c_bool()
        )

        self.bone_name = _GetSkeletonBoneNameC(rig_bone).decode('utf-8').strip()
        self.PtrSetBoneTranslation(rig_bone)
        self.PtrSetBoneRotation(rig_bone)
        self.PtrSetBoneParent(rig_bone, rig_ptr)
        self.PtrSetBoneMapping(rig_ptr)
        self.index = b_idx  # TODO

        self.PtrSetBoneAttributes(rig_bone)

    def LoadBoneFromArmature(self, edit_bone, index=-1):
        """
        Loads bone from Blender armature
        """
        self.bone_name = edit_bone.name
        self.parent_name = edit_bone.parent.name if edit_bone.parent != None else None
        self.parent_index = edit_bone.parent.sf_bone_props.index if edit_bone.parent != None else -1
        self.index = index  # TODO
        self.LoadArmatureBoneAttributes(edit_bone)


class RigBoneRotation:
    def __init__(self, rotation_xyzw=None):
        if rotation_xyzw is not None:
            self.x = rotation_xyzw[0]
            self.y = rotation_xyzw[1]
            self.z = rotation_xyzw[2]
            self.w = rotation_xyzw[3]
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
