from AnimationIO.AnimationIOFuncs import (
    _GetSkeletonBoneNameC, _GetGlobalSkeletonBonePositionC, _GetVector3XC, _GetVector3YC, _GetVector3ZC,
    _GetGlobalSkeletonBoneRotationC, _GetQuaternionXC, _GetQuaternionYC, _GetQuaternionZC, _GetQuaternionWC,
    _GetBoneTypeAsStringC, _GetTwistBoneDriverC, _GetTwistBoneDriverWeightC, _GetScalarSqSizeC, _GetScalarFromSqC,
    _GetFrameFromScalarFrameC, _GetValueFromScalarFrameC, _GetRotationSqSizeC, _GetRotationFromSqC,
    _GetValueFromRotationFrameC, _GetFrameFromRotationFrameC, _GetTranslationSqSizeC, _GetTranslationFromSqC,
    _GetValueFromTranslationFrameC, _GetFrameFromTranslationFrameC, _GetVector3DXC, _GetVector3DYC, _GetVector3DZC,
    _SFBGSRigPackage_GetBoneLODValueC, _SFBGSRigPackage_AddBoneToMapC, _SetBoneTypeFromStringC,
    _SetTwistBonePropertiesC, _SFBGSRigPackage_SetBoneLODValueC, _SetBoneTypeC, _SFBGSRigPackage_GetBoneKeyC,
    _SFBGSRigPackage_AddBoneNameToMapC,
)
from AnimationIO.BoneMatrix import BoneMatrix
from mathutils import Vector, Quaternion, Matrix

def get_bone_type_int(s):
    s = s.upper()

    if s == "TWIST":
        return 1
    return 0

class AnimatedBone:
    def __init__(self, bone_name):
        self.name = bone_name
        self.parent_name = None
        self.matrix = BoneMatrix()

        # attr
        self.mirror_name = None # unused
        self.bone_type = None # string
        self.twist_bone_driver_weight = 0.0
        self.twist_bone_driver_name = None
        self.lod_value = None
        self.mapped_to = None
        #self.mirror_bone_name = None

    def clear(self):
        self.matrix.clear_overlay_matrix()

    def __repr__(self):
        return f"AnimatedBone {self.name}\n{self.matrix}"

    def from_anim_block_ptr(self, anim_block_ptr):
        def fill_dict(dictionary, key, init_data_key, init_data_val):
            """small helper"""
            if key not in dictionary:
                dictionary[key] = {}
            dictionary[key][init_data_key] = init_data_val

        data = {}

        sqs_size = _GetScalarSqSizeC(anim_block_ptr)
        for s in range(sqs_size):
            sqs = _GetScalarFromSqC(anim_block_ptr, s)
            frame_id = _GetFrameFromScalarFrameC(sqs)
            scale_uniform = _GetValueFromScalarFrameC(sqs)
            fill_dict(data, frame_id, "sca", scale_uniform)

        rsq_size = _GetRotationSqSizeC(anim_block_ptr)
        for r in range(rsq_size):
            rsq = _GetRotationFromSqC(anim_block_ptr, r)
            rsq_val = _GetValueFromRotationFrameC(rsq)
            frame_id = _GetFrameFromRotationFrameC(rsq)
            r_x = _GetQuaternionXC(rsq_val)
            r_y = _GetQuaternionYC(rsq_val)
            r_z = _GetQuaternionZC(rsq_val)
            r_w = _GetQuaternionWC(rsq_val)
            fill_dict(data, frame_id, "rot", (r_w, r_x, r_y, r_z))

        tsq_size = _GetTranslationSqSizeC(anim_block_ptr)
        for t in range(tsq_size):
            tsq = _GetTranslationFromSqC(anim_block_ptr, t)
            tsq_val = _GetValueFromTranslationFrameC(tsq)
            frame_id = _GetFrameFromTranslationFrameC(tsq)
            t_x = _GetVector3DXC(tsq_val)
            t_y = _GetVector3DYC(tsq_val)
            t_z = _GetVector3DZC(tsq_val)
            fill_dict(data, frame_id, "tra", (t_x, t_y, t_z))

        for frame_id, bone_data in data.items():
            mask = [False, False, False]

            bone_tra = Vector((0.0, 0.0, 0.0))
            if "tra" in bone_data.keys():
                mask[0] = True
                bone_tra = Vector(bone_data["tra"])

            bone_rot = Quaternion((1.0, 0.0, 0.0, 0.0))
            if "rot" in bone_data.keys():
                mask[1] = True
                bone_rot = Quaternion(bone_data["rot"])

            bone_sca = Matrix.Scale(1.0, 4, (1.0, 1.0, 1.0))
            if "sca" in bone_data.keys():
                mask[2] = True
                bone_sca = Matrix.Scale(
                    1.0, 4, (bone_data["sca"], bone_data["sca"], bone_data["sca"]))

            self.matrix.set_overlay_matrix(frame_id, (bone_tra, bone_rot, bone_sca), mask)

    def from_rig_bone_ptr(self, rig_ptr, bone_ptr):
        """
        Loads Name, Translation, Rotation from
        rig bone to bone's world matrix.

        Parent is not set!
        """

        self.name = _GetSkeletonBoneNameC(bone_ptr).decode('utf-8').strip()

        # translation
        ptr_tra = _GetGlobalSkeletonBonePositionC(bone_ptr)
        tra_x = _GetVector3XC(ptr_tra)
        tra_y = _GetVector3YC(ptr_tra)
        tra_z = _GetVector3ZC(ptr_tra)
        #_DeleteVector3C(ptr_tra) # heap corruption

        # rotation
        ptr_rot = _GetGlobalSkeletonBoneRotationC(bone_ptr)

        rot_x = _GetQuaternionXC(ptr_rot)
        rot_y = _GetQuaternionYC(ptr_rot)
        rot_z = _GetQuaternionZC(ptr_rot)
        rot_w = _GetQuaternionWC(ptr_rot)
        # _DeleteQuaternionC(ptr_rot) # access violation

        self.matrix.world_bone_matrix = (
            Vector((tra_x, tra_y, tra_z)),
            Quaternion((rot_w, rot_x, rot_y, rot_z))
        )

        self.bone_type = _GetBoneTypeAsStringC(bone_ptr).decode('utf-8')

        if self.bone_type == "Twist":
            self.twist_bone_driver_weight = _GetTwistBoneDriverWeightC(bone_ptr)
            self.twist_bone_driver_name = _GetTwistBoneDriverC(bone_ptr).decode('utf-8')

        self.lod_value = _SFBGSRigPackage_GetBoneLODValueC(rig_ptr, self.name.encode('utf-8'))
        self.mapped_to = _SFBGSRigPackage_GetBoneKeyC(rig_ptr, self.name.encode('utf-8'))
        #self.mirror_bone_name =
        #_SFBGSRigPackage_AddBoneToMapC(
        #    rig_ptr,
        #    bone_ptr,
        #    self.mapped_to
        #)
        # TODO

    def to_blender_bone(self, blender_bone):
        """
        Expects edit mode
        Doesn't set name, or parent.
        """
        blender_bone.name = self.name
        blender_bone.length = 0.07

        blender_bone.matrix = self.matrix.blender_compatible_bone_world_matrix

        blender_bone.sf_bone_props.do_correct_bone = True

        self.set_rig_bone_attr(blender_bone)

        # to test correction
        #self.matrix.blender_compatible_bone_world_matrix = blender_bone.matrix
        #blender_bone.matrix = self.matrix.blender_compatible_bone_world_matrix

    def from_blender(self, edit_bone):
        """Create rig bone from Blender"""

        self.name = edit_bone.name
        self.parent_name = edit_bone.parent.name if edit_bone.parent is not None else None
        self.matrix.blender_compatible_bone_world_matrix = edit_bone.matrix
        self.get_rig_bone_attr(edit_bone)

    def from_anim_pose_bone(self, pose_bone, frame_id):
        import bpy

        self.matrix.set_overlay_matrix_from_blender(frame_id, pose_bone.matrix_basis, [True, True, True])

    def provide_anim_to_pose_bone(self, pose_bone, max_keyframe_idx):
        """Adds animation to Blender pose bone"""
        for frame_id in range(max_keyframe_idx):
            has_data, matrix = self.matrix.get_blender_compatible_overlay_matrix(frame_id)
            pose_bone.matrix_basis = Matrix.Identity(4)

            if has_data:
                pose_bone.matrix_basis = matrix

                if self.matrix._overlay_matrices_mask[frame_id][0]:
                    pose_bone.keyframe_insert(data_path='location', frame=frame_id)

                if self.matrix._overlay_matrices_mask[frame_id][1]:
                    pose_bone.keyframe_insert(data_path='rotation_quaternion', frame=frame_id)

                if self.matrix._overlay_matrices_mask[frame_id][2]:
                    pose_bone.keyframe_insert(data_path='scale', frame=frame_id)

    def load_onto_ptr(self, rig_ptr, bone_ptr):
        _SetBoneTypeC(bone_ptr, get_bone_type_int(self.bone_type))

        if self.bone_type == "Twist":
            _SetTwistBonePropertiesC(bone_ptr, True, self.twist_bone_driver_name.encode('utf-8'), self.twist_bone_driver_weight)

        _SFBGSRigPackage_SetBoneLODValueC(rig_ptr, self.name.encode('utf-8'), self.lod_value)
        mapped_to = int(self.mapped_to)
        if mapped_to != 255:
            _SFBGSRigPackage_AddBoneNameToMapC(rig_ptr, mapped_to, self.name.encode('utf-8'), True)

    def set_rig_bone_attr(self, blender_bone):
        """Expects edit mode"""
        blender_bone.sf_bone_props.bone_type = self.bone_type
        #print(self.bone_type)
        if self.bone_type == "Twist":
            blender_bone.sf_bone_props.twist_bone_driver_weight = self.twist_bone_driver_weight
            blender_bone.sf_bone_props.twist_bone_driver_name = self.twist_bone_driver_name

        blender_bone.sf_bone_props.lod_value = self.lod_value
        blender_bone.sf_bone_props.mapping = str(self.mapped_to)

    def get_rig_bone_attr(self, blender_bone):
        """Expects edit mode"""
        self.bone_type = blender_bone.sf_bone_props.bone_type
        #print(self.bone_type)
        if self.bone_type == "Twist":
            self.twist_bone_driver_weight = blender_bone.sf_bone_props.twist_bone_driver_weight
            self.twist_bone_driver_name = blender_bone.sf_bone_props.twist_bone_driver_name

        self.lod_value = blender_bone.sf_bone_props.lod_value
        self.mapped_to = int(blender_bone.sf_bone_props.mapping)
