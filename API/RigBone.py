import ctypes
import bpy
import mathutils

from API.AnimConverterFunc import (
    _GetTwistBoneDriverWeightC, _GetSkeletonBoneC, _GetSkeletonBoneNameC, _GetGlobalSkeletonBonePositionC,
    _GetVector3XC, _GetVector3YC, _GetVector3ZC, _GetQuaternionXC, _GetQuaternionYC, _GetQuaternionZC, _GetQuaternionWC,
    _GetGlobalSkeletonBoneRotationC, _GetTwistBoneDriverC, _GetBoneTypeC)


class RigBone:
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
        self.twist_bone_driver_name = None
        self.bone_name = None
        self.rotation = RigBoneRotation()
        self.translation = None #todo translation class

        self.parent_name = None
        self.parent_index = None # deprecate it!

        self.index = None

        self.rig_bone_index = None
        self.mirror_index = -1
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

    def get_matrix(self):
        tra = mathutils.Matrix.Translation(self.translation)
        rot = mathutils.Quaternion(self.rotation.raw_wxyz).to_matrix().to_4x4()
        sca = mathutils.Matrix.Scale(1.000, 4, [1.0, 1.0, 1.0])
        return tra @ rot @ sca

    def set_from_matrix(self, matrix):
        tra, rot, _ = matrix.decompose()
        self.translation = tra
        self.rotation.raw_wxyz = (rot.w, rot.x, rot.y, rot.z)

    def set_attributes_from_ptr(self, rig_bone_ptr):
        """Sets bone attributes"""
        self.rig_bone_index = self.index # TODO TODO
        #self.mirror_index = _GetMirrorIndexC(rig_bone_ptr)
        self.twist_bone_driver_name = _GetTwistBoneDriverC(rig_bone_ptr) # TODO
        self.twist_bone_driver_weight = _GetTwistBoneDriverWeightC(rig_bone_ptr)
        #self.bone_type = _GetBoneTypeC(rig_bone_ptr) TODO

    def set_parent_from_ptr(self, rig_bone, parent_name):
        """Sets bone parent name and index"""
        self.parent_name = parent_name

    def set_rotation_from_ptr(self, rig_bone):
        """Sets bone rotation from ptr"""
        bone_r = _GetGlobalSkeletonBoneRotationC(rig_bone)

        self.rotation.x = _GetQuaternionXC(bone_r)
        self.rotation.y = _GetQuaternionYC(bone_r)
        self.rotation.z = _GetQuaternionZC(bone_r)
        self.rotation.w = _GetQuaternionWC(bone_r)

    def set_translation_from_ptr(self, rig_bone):
        """Sets bone translation from ptr"""
        bone_t = _GetGlobalSkeletonBonePositionC(rig_bone)

        x = _GetVector3XC(bone_t)
        y = _GetVector3YC(bone_t)
        z = _GetVector3ZC(bone_t)

        self.translation = (x, y, z)

    # Deprecated as mapping is no longer managed by the user.
    # def set_bone_mapping_from_ptr(self, rig_ptr):
    #     """Sets bone mapping from ptr"""
    #     if _SFBGSRigPackage_BoneIsMappedC(rig_ptr, self.bone_name.encode('utf-8')):
    #         self.mapping = _SFBGSRigPackage_GetBoneKeyC(rig_ptr, self.bone_name.encode('utf-8'))

    def set_blender_bone_attr(self, armature_bone : bpy.types.EditBone):
        """Sets Blender armature bone attributes"""
        #armature_bone.sf_bone_props.index = self.index
        armature_bone.sf_bone_props.mirror_index = self.mirror_index
        armature_bone.sf_bone_props.bone_type = str(self.bone_type_blender)
        armature_bone.sf_bone_props.twist_bone_driver_weight = self.twist_bone_driver_weight
        armature_bone.sf_bone_props.mapping = str(self.mapping)

        if RigBone.bone_types[self.bone_type] == "Twist":
            armature_bone.sf_bone_props.twist_bone_driver_name = self.twist_bone_driver_name
            armature_bone.sf_bone_props.twist_bone_driver_weight = self.twist_bone_driver_weight

    def from_blender(self, edit_bone : bpy.types.EditBone):
        """Loads bone from Blender armature"""
        self.bone_name = edit_bone.name
        self.parent_name = edit_bone.parent.name if edit_bone.parent != None else None
        self.parent_index = edit_bone.parent.sf_bone_props.index if edit_bone.parent != None else -1
        #self.index = edit_bone.sf_bone_props.index
        #self.mirror_index = edit_bone.sf_bone_props.mirror_index
        self.bone_type_blender = edit_bone.sf_bone_props.bone_type
        self.mapping = int(edit_bone.sf_bone_props.mapping)

        if edit_bone.sf_bone_props.bone_type == "Twist":
            self.twist_bone_driver_name = edit_bone.sf_bone_props.twist_bone_driver_name
            self.twist_bone_driver_weight = edit_bone.sf_bone_props.twist_bone_driver_weight

        self.set_from_matrix(edit_bone.matrix)

    def from_ptr(self, bone_ptr : int, parent_bone_name):
        """Loads bone from rig pointer"""

        self.bone_name = _GetSkeletonBoneNameC(bone_ptr).decode('utf-8').strip()
        self.set_translation_from_ptr(bone_ptr)
        self.set_rotation_from_ptr(bone_ptr)
        self.set_parent_from_ptr(bone_ptr, parent_bone_name)
        self.index = None

        self.set_attributes_from_ptr(bone_ptr)

    def to_ptr(self, rig_ptr, bone_index : int):
        """Returns bone pointer"""
        _AddBoneToSkeletonRigC(
            rig_ptr,
            self.rotation.x,
            self.rotation.y,
            self.rotation.z,
            self.rotation.w,

            self.translation[0],  # x
            self.translation[1],  # y
            self.translation[2],  # z

            self.bone_name.encode('utf-8'),

            self.parent_index if self.parent_index is not None else -1,

            ctypes.c_bool(True),

            cont
        )

        bone_ptr = _GetSkeletonBoneC(rig_ptr, bone_index, ctypes.c_bool(False))

        if self.mapping != 255:
            if not _SFBGSRigPackage_AddBoneNameToMapC(
                    rig_ptr,
                    self.mapping,
                    self.bone_name.encode('utf-8'),
                    cont,
                    ctypes.c_bool(False)):
                print((
                    rig_ptr,
                    self.mapping,
                    self.bone_name.encode('utf-8'),
                    cont,
                    ctypes.c_bool(False)
                ))
                raise Exception(_GetStringFromContainerC(cont).decode('utf-8'))

        _SetBoneTypeC(bone_ptr, self.bone_type)
        _SetMirrorIndexC(bone_ptr, self.mirror_index)

        # TODO BELOW
        if self.bone_type_blender == "Twist":
            _SetTwistBonePropertiesC(bone_ptr, ctypes.c_bool(True),
                                     self.twist_bone_driver_name, self.twist_bone_driver_weight, cont)

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

    @raw_wxyz.setter
    def raw_wxyz(self, value):
        self.x = value[0]
        self.y = value[1]
        self.z = value[2]
        self.w = value[3]