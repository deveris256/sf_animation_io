import ctypes
from enum import Enum
import mathutils

from AnimationIO.AnimationIOFuncs import (
    _GetSkeletonBoneNameC, _GetSkeletonRigBoneCountC, _GetSkeletonBoneChildC,
    _GetSkeletonRigRootC, _LoadSFBGSSkeletonRigFromFileC, _GetAnimationBlockC, _GetScalarSqSizeC, _GetScalarFromSqC,
    _GetFrameFromScalarFrameC, _GetValueFromScalarFrameC, _GetTranslationSqSizeC, _GetTranslationFromSqC,
    _GetFrameFromTranslationFrameC, _GetVector3DXC, _GetVector3DYC, _GetVector3DZC, _GetRotationSqSizeC,
    _GetRotationFromSqC, _GetFrameFromRotationFrameC, _GetQuaternionXC, _GetQuaternionYC, _GetQuaternionZC,
    _GetQuaternionWC, _list_to_wchar_arr, _LoadAnimationSceneFromSFBGSFormatC, _GetAnimationWithIndexC,
    _GetValueFromRotationFrameC, _GetValueFromTranslationFrameC, _CreateSkeletonRigC, _AddChildBoneC,
    _SaveSkeletonRigToSFBGSFormatDirectC, _SFBGSRigPackage_GetPrecisionType, _SFBGSRigPackage_AddPackageToSkeletonRigC,
    _SFBGSRigPackage_IsMannequinC, _SFBGSRigPackage_SetMannequinC, _SFBGSRigPackage_SetPrecisionToDefaultC,
    _SFBGSRigPackage_SetPrecisionToShipValuesC, _SFBGSRigPackage_SetPrecisionToFirstPersonC, _RenameBoneC,
    _SetGlobalSkeletonBoneRotationC, _SetLocalSkeletonBoneRotationC, _UNIVMirrorRigPackage_AddPackageToSkeletonRigC,
    _SetGlobalSkeletonBonePositionC,
)
from AnimationIO.AnimatedBone import AnimatedBone
from CommonUtils import ensure_object_mode, ensure_bl_mode_on_obj

class RigPrecision:
    rig_precision = {
        "DEFAULT": 0,
        "FIRST PERSON": 1,
        "SHIP": 2,
        "CUSTOM": 3
    }

    rig_precision_inv = {v: k for k, v in rig_precision.items()}

    def __init__(self, val):
        self.set_precision(val)
        self._custom_rig_precision = 0.03125
        self._precision = 0

    def set_precision(self, val, custom=None):
        if isinstance(val, str):
            if val.isdigit():
                val = int(val)
            else:
                val = RigPrecision.rig_precision[val]

        if not val in RigPrecision.rig_precision.values():
            raise Exception(f"Invalid rig precision: {val}")

        self._precision = val

        if self._precision == 3:
            self._custom_rig_precision = float(custom) if custom is not None else 0.03125 # default precision

    @property
    def precision_int(self):
        return self._precision

    @precision_int.setter
    def precision_int(self, val):
        self.set_precision(val)

    @property
    def precision_str(self):
        return self.rig_precision_inv[self._precision]

    @precision_str.setter
    def precision_str(self, val):
        self.set_precision(val)

class AnimatableRig:
    def __init__(self):
        self.precision = RigPrecision(0)
        self.bones = []
        self.has_animation = False
        self.is_mannequin = False

    def clear_anim(self):
        for bone in self.bones:
            bone.clear()

    def anim_from_ptr(self, anim_scene_ptr):
        print("anim_from_ptr")
        self.has_animation = True

        # TODO: Currently loads first animation from af
        anim_ptr = _GetAnimationWithIndexC(
            anim_scene_ptr,
            0,
        )

        for bone in self.bones:
            block_name = bone.name

            anim_block_ptr = _GetAnimationBlockC(
                anim_ptr,
                block_name.encode('utf-8')
            )

            bone.from_anim_block_ptr(anim_block_ptr)

    def rig_from_ptr(self, rig_ptr):
        """Secondary ctor"""
        print("Rig ptr", rig_ptr)
        precision_str = _SFBGSRigPackage_GetPrecisionType(rig_ptr).decode('utf-8').upper()
        self.precision.precision_str = precision_str

        self.is_mannequin = _SFBGSRigPackage_IsMannequinC(rig_ptr)

        bone_count = _GetSkeletonRigBoneCountC(rig_ptr)

        root_bone = _GetSkeletonRigRootC(rig_ptr)
        root_bone_name = self._load_single_bone(rig_ptr, None, root_bone)
        self._load_ptr_bones_recursive(rig_ptr, root_bone, root_bone_name, bone_count)

    def _load_single_bone(self, rig_ptr, root_bone_name, bone_ptr):
        """Loads single rig bone"""
        bone_name = _GetSkeletonBoneNameC(bone_ptr).decode('utf-8')

        animated_bone = AnimatedBone(bone_name)
        animated_bone.from_rig_bone_ptr(rig_ptr, bone_ptr)
        animated_bone.parent_name = root_bone_name
        self.bones.append(animated_bone)
        return bone_name

    def _load_ptr_bones_recursive(self, rig_ptr, root_bone_ptr, root_bone_name, bone_count):
        """Recursively loads rig bones from pointer"""
        for bone_idx in range(bone_count):
            bone_ptr = _GetSkeletonBoneChildC(root_bone_ptr, bone_idx)
            if bone_ptr is None: break

            bone_name = self._load_single_bone(rig_ptr, root_bone_name, bone_ptr)

            self._load_ptr_bones_recursive(rig_ptr, bone_ptr, bone_name, bone_count)

    def from_blender(self, rig_obj):
        ensure_bl_mode_on_obj('EDIT', rig_obj)

        self.precision.set_precision(rig_obj.sf_rig_props.rig_precision)
        self.is_mannequin = rig_obj.sf_rig_props.is_mannequin

        for edit_bone in rig_obj.data.edit_bones:
            bone = AnimatedBone(edit_bone.name)
            bone.from_blender(edit_bone)
            self.bones.append(bone)

        ensure_object_mode()

    def rig_to_blender(self, armature_obj):
        """Manages modes on its own."""
        armature_obj.sf_rig_props.is_rig = True
        ensure_bl_mode_on_obj('EDIT', armature_obj)

        armature_obj.sf_rig_props.precision = self.precision.precision_str
        armature_obj.sf_rig_props.is_mannequin = self.is_mannequin

        for bone in self.bones:
            blender_bone = armature_obj.data.edit_bones.new(name=bone.name)
            bone.to_blender_bone(blender_bone)

        # parents pass
        edit_bones = armature_obj.data.edit_bones
        for bone in edit_bones:
            animatable_bone =\
                [b for b in self.bones if b.name == bone.name][0]

            if animatable_bone.parent_name is not None:
                bone.parent =\
                    [b for b in edit_bones if b.name == animatable_bone.parent_name][0]

    def anim_to_blender(self, armature_obj):
        #import bpy
        #import math
        #import mathutils

        armature_obj.sf_rig_props.is_anim = True
        ensure_bl_mode_on_obj('POSE', armature_obj)

        max_keyframe_idx = 0
        for b in self.bones:
            if len(b.matrix._overlay_matrices.keys()) > 0:
                max_keyframe_idx = max((max_keyframe_idx, max(b.matrix._overlay_matrices.keys())))
        max_keyframe_idx += 1

        # this comment should exist:
        #axes = ['X', 'Y', 'Z']
        #corrections = [90, -90, 180, -180]
        #for axisA in axes:
        #    for rotationA in corrections:
        #        for axisB in axes:
        #            for rotationB in corrections:
        #                ###
        #                new_armature_obj = armature_obj.copy()
        #                new_armature_obj.data = armature_obj.data.copy()
        #                new_armature_obj.name = f"A_{axisA}{rotationA} B_{axisB}{rotationB}"
        #                bpy.context.collection.objects.link(new_armature_obj)
        #                corrA = mathutils.Matrix.Rotation(math.radians(rotationA), 4, axisA)
        #                corrB = mathutils.Matrix.Rotation(math.radians(rotationB), 4, axisB)

        for bone in self.bones:
            pose_bone = armature_obj.pose.bones.get(bone.name)
            bone.provide_anim_to_pose_bone(pose_bone, max_keyframe_idx)

    def rig_to_ptr(self):
        rig_ptr = _CreateSkeletonRigC("skeleton".encode('utf-8'))

        _SFBGSRigPackage_AddPackageToSkeletonRigC(rig_ptr, True)
        _UNIVMirrorRigPackage_AddPackageToSkeletonRigC(rig_ptr, True)
        _SFBGSRigPackage_SetMannequinC(rig_ptr, ctypes.c_bool(self.is_mannequin))

        root_bone = _GetSkeletonRigRootC(rig_ptr)
        rig_root_bone = [b for b in self.bones if b.parent_name is None][0]
        _RenameBoneC(rig_ptr, _GetSkeletonBoneNameC(root_bone), rig_root_bone.name.encode('utf-8'))

        _add_bones_recursive(self, rig_ptr, root_bone, [b for b in self.bones if b.parent_name == rig_root_bone.name])

        match self.precision.precision_str.lower():
            case "ship": _SFBGSRigPackage_SetPrecisionToShipValuesC(rig_ptr)
            case "first_person": _SFBGSRigPackage_SetPrecisionToFirstPersonC(rig_ptr)
            case "custom": raise NotImplementedError("Custom rig precision is not yet implemented.") #TODO
            case _: _SFBGSRigPackage_SetPrecisionToDefaultC(rig_ptr)

        return rig_ptr


def get_rig_ptr_and_rig(rig_path):
    rig = AnimatableRig()
    print("Importing rig from", rig_path)
    rig_ptr = _LoadSFBGSSkeletonRigFromFileC(
        ctypes.c_wchar_p(rig_path)
    )
    rig.rig_from_ptr(rig_ptr)
    return rig_ptr, rig

def create_rig_armature(rig):
    import bpy
    ensure_object_mode()

    armature_data = bpy.data.armatures.new(name="armature")
    armature_obj = bpy.data.objects.new(name="armature_obj", object_data=armature_data)
    bpy.context.collection.objects.link(armature_obj)

    ensure_bl_mode_on_obj("EDIT", armature_obj)

    rig.rig_to_blender(armature_obj)
    ensure_object_mode()
    return armature_obj

def bl_import_rig_from_path(rig_path):
    _, rig = get_rig_ptr_and_rig(rig_path)
    create_rig_armature(rig)


def _add_bones_recursive(rig, rig_ptr, parent_bone_ptr, child_bones):
    print(rig, parent_bone_ptr, child_bones)
    for bone in child_bones:
        bone_mat = bone.matrix.world_bone_matrix

        #if bone.parent_name:
        #    parent = [b for b in rig.bones if b.name == bone.parent_name][0]
        #    parent_mat = parent.matrix.world_bone_matrix
        #    bone_mat = parent_mat.inverted() @ bone_mat

        tra, rot, sca = bone_mat.decompose()

        bone_ptr = _AddChildBoneC(
            parent_bone_ptr,
            tra.x, tra.y, tra.z,
            rot.x, rot.y, rot.z, rot.w,
            bone.name.encode('utf-8')
        )
        _SetGlobalSkeletonBoneRotationC(bone_ptr, rot.x, rot.y, rot.z, rot.w)
        _SetGlobalSkeletonBonePositionC(bone_ptr, tra.x, tra.y, tra.z)

        bone.load_onto_ptr(rig_ptr, bone_ptr)

        new_child_bones = [b for b in rig.bones if b.parent_name == bone.name]
        if len(new_child_bones) != 0:
            _add_bones_recursive(rig, rig_ptr, bone_ptr, new_child_bones)

def bl_export_rig_from_path(rig_obj, rig_path):
    rig = AnimatableRig()
    rig.from_blender(rig_obj)

    rig_ptr = rig.rig_to_ptr()

    _SaveSkeletonRigToSFBGSFormatDirectC(rig_ptr, ctypes.c_wchar_p(rig_path))

def bl_import_anim_from_path(anim_path, rig, rig_path, rig_bl_obj):
    import bpy
    ensure_object_mode()

    rig_anim_paths = [rig_path, anim_path]
    wchars = _list_to_wchar_arr(rig_anim_paths)

    anim_scene = _LoadAnimationSceneFromSFBGSFormatC(
        wchars,
        len(rig_anim_paths),
    )
    rig.clear_anim()
    rig.anim_from_ptr(anim_scene)
    ensure_bl_mode_on_obj("POSE", rig_bl_obj)
    rig.anim_to_blender(rig_bl_obj)
