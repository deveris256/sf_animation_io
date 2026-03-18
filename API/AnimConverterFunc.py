import ctypes
import os

_anim_dll = ctypes.CDLL(os.path.join(os.path.dirname(os.path.dirname(__file__)),'CALUMI.Animation.dll'))
PATH_FOR_IMPORT_JSON = "C:\\General Files\\Git\\AnimScript\\AnimStarfieldMeshConverter_repo\\scripts\\tool_export_mesh\\ExportedJSONs\\LastFile.json"

def _list_to_wchar_arr(python_list):
    arr = (ctypes.c_wchar_p * len(python_list))()
    arr[:] = python_list
    return arr

_CreateAnimationC = _anim_dll.CreateAnimationC
_CreateAnimationC.restype = ctypes.c_void_p # Animation *

_CreateAnimationC.argtypes = [
ctypes.c_char_p,
ctypes.c_uint, # unsigned int
]

_GetAnimationBlockC = _anim_dll.GetAnimationBlockC
_GetAnimationBlockC.restype = ctypes.c_void_p # AnimationBlock *

_GetAnimationBlockC.argtypes = [
ctypes.c_void_p, # Animation *
ctypes.c_int,
ctypes.c_bool, # Utilities::StringContainer *
]

_GetAnimationBlockCountC = _anim_dll.GetAnimationBlockCountC
_GetAnimationBlockCountC.restype = ctypes.c_size_t
_GetAnimationBlockCountC.argtypes = [
ctypes.c_void_p, # Animation *
]

_GetAnimationTitleC = _anim_dll.GetAnimationTitleC
_GetAnimationTitleC.restype = ctypes.c_char_p
_GetAnimationTitleC.argtypes = [
ctypes.c_void_p, # Animation *
]

_GetFrameCountC = _anim_dll.GetFrameCountC
_GetFrameCountC.restype = ctypes.c_size_t
_GetFrameCountC.argtypes = [
ctypes.c_void_p, # Animation *
]

_DeleteAnimationC = _anim_dll.DeleteAnimationC
_DeleteAnimationC.restype = ctypes.c_bool
_DeleteAnimationC.argtypes = [
ctypes.c_void_p, # Animation *
]

_AddAnimBlockToAnimationC = _anim_dll.AddAnimBlockToAnimationC
_AddAnimBlockToAnimationC.restype = ctypes.c_bool
_AddAnimBlockToAnimationC.argtypes = [
ctypes.c_void_p, # Animation *
ctypes.c_void_p, # AnimationBlock *
ctypes.c_bool,
ctypes.c_bool, # Utilities::StringContainer *
]

_CreateAnimBlockC = _anim_dll.CreateAnimBlockC
_CreateAnimBlockC.restype = ctypes.c_void_p # AnimationBlock *

_CreateAnimBlockC.argtypes = [
ctypes.c_char_p,
ctypes.c_int,
ctypes.c_bool, # Utilities::StringContainer *
]

_DeleteAnimationBlockC = _anim_dll.DeleteAnimationBlockC
_DeleteAnimationBlockC.restype = ctypes.c_bool
_DeleteAnimationBlockC.argtypes = [
ctypes.c_void_p, # AnimationBlock *
]

_GetAnimBlockBoneNameC = _anim_dll.GetAnimBlockBoneNameC
_GetAnimBlockBoneNameC.restype = ctypes.c_char_p
_GetAnimBlockBoneNameC.argtypes = [
ctypes.c_void_p, # AnimationBlock *
]

_GetAnimBlockBoneIndexC = _anim_dll.GetAnimBlockBoneIndexC
_GetAnimBlockBoneIndexC.restype = ctypes.c_int
_GetAnimBlockBoneIndexC.argtypes = [
ctypes.c_void_p, # AnimationBlock *
]

_GetLastFrameInAnimBlockC = _anim_dll.GetLastFrameInAnimBlockC
_GetLastFrameInAnimBlockC.restype = ctypes.c_uint

_GetLastFrameInAnimBlockC.argtypes = [
ctypes.c_void_p, # AnimationBlock *
]

_AddRotationSqToAnimBlockC = _anim_dll.AddRotationSqToAnimBlockC
_AddRotationSqToAnimBlockC.restype = ctypes.c_bool
_AddRotationSqToAnimBlockC.argtypes = [
ctypes.c_void_p, # AnimationBlock *
ctypes.c_void_p, # Rotation *
ctypes.c_uint,
ctypes.c_bool,
]

_GetRotationSqArrayC = _anim_dll.GetRotationSqArrayC
_GetRotationSqArrayC.restype = ctypes.c_void_p # Rotation *

_GetRotationSqArrayC.argtypes = [
ctypes.c_void_p, # AnimationBlock *
]

_GetRotationFromSqC = _anim_dll.GetRotationFromSqC
_GetRotationFromSqC.restype = ctypes.c_void_p # Rotation *

_GetRotationFromSqC.argtypes = [
ctypes.c_void_p, # AnimationBlock *
ctypes.c_int,
ctypes.c_bool, # Utilities::StringContainer *
]

_GetRotationSqSizeC = _anim_dll.GetRotationSqSizeC
_GetRotationSqSizeC.restype = ctypes.c_size_t
_GetRotationSqSizeC.argtypes = [
ctypes.c_void_p, # AnimationBlock *
]

_AddTranslationSqToAnimBlockC = _anim_dll.AddTranslationSqToAnimBlockC
_AddTranslationSqToAnimBlockC.restype = ctypes.c_bool
_AddTranslationSqToAnimBlockC.argtypes = [
ctypes.c_void_p, # AnimationBlock *
ctypes.c_void_p, # Translation *
ctypes.c_uint,
ctypes.c_bool,
]

_GetTranslationSqArrayC = _anim_dll.GetTranslationSqArrayC
_GetTranslationSqArrayC.restype = ctypes.c_void_p # Translation *

_GetTranslationSqArrayC.argtypes = [
ctypes.c_void_p, # AnimationBlock *
]

_GetTranslationFromSqC = _anim_dll.GetTranslationFromSqC
_GetTranslationFromSqC.restype = ctypes.c_void_p # Translation *

_GetTranslationFromSqC.argtypes = [
ctypes.c_void_p, # AnimationBlock *
ctypes.c_int,
ctypes.c_bool, # Utilities::StringContainer *
]

_GetTranslationSqSizeC = _anim_dll.GetTranslationSqSizeC
_GetTranslationSqSizeC.restype = ctypes.c_size_t
_GetTranslationSqSizeC.argtypes = [
ctypes.c_void_p, # AnimationBlock *
]

_AddScalarSqToAnimBlockC = _anim_dll.AddScalarSqToAnimBlockC
_AddScalarSqToAnimBlockC.restype = ctypes.c_bool
_AddScalarSqToAnimBlockC.argtypes = [
ctypes.c_void_p, # AnimationBlock *
ctypes.c_void_p, # Scalar *
ctypes.c_uint,
ctypes.c_bool,
]

_GetScalarSqArrayC = _anim_dll.GetScalarSqArrayC
_GetScalarSqArrayC.restype = ctypes.c_void_p # Scalar *

_GetScalarSqArrayC.argtypes = [
ctypes.c_void_p, # AnimationBlock *
]

_GetScalarFromSqC = _anim_dll.GetScalarFromSqC
_GetScalarFromSqC.restype = ctypes.c_void_p # Scalar *

_GetScalarFromSqC.argtypes = [
ctypes.c_void_p, # AnimationBlock *
ctypes.c_int,
ctypes.c_bool, # Utilities::StringContainer *
]

_GetScalarSqSizeC = _anim_dll.GetScalarSqSizeC
_GetScalarSqSizeC.restype = ctypes.c_size_t
_GetScalarSqSizeC.argtypes = [
ctypes.c_void_p, # AnimationBlock *
]

_AddPrioritySqToAnimBlockC = _anim_dll.AddPrioritySqToAnimBlockC
_AddPrioritySqToAnimBlockC.restype = ctypes.c_bool
_AddPrioritySqToAnimBlockC.argtypes = [
ctypes.c_void_p, # AnimationBlock *
ctypes.c_void_p, # Priority *
ctypes.c_uint,
ctypes.c_bool,
]

_GetPrioritySqArrayC = _anim_dll.GetPrioritySqArrayC
_GetPrioritySqArrayC.restype = ctypes.c_void_p # Priority *

_GetPrioritySqArrayC.argtypes = [
ctypes.c_void_p, # AnimationBlock *
]

_GetPriorityFromSqC = _anim_dll.GetPriorityFromSqC
_GetPriorityFromSqC.restype = ctypes.c_void_p # Priority *

_GetPriorityFromSqC.argtypes = [
ctypes.c_void_p, # AnimationBlock *
ctypes.c_int,
ctypes.c_bool, # Utilities::StringContainer *
]

_GetPrioritySqSizeC = _anim_dll.GetPrioritySqSizeC
_GetPrioritySqSizeC.restype = ctypes.c_size_t
_GetPrioritySqSizeC.argtypes = [
ctypes.c_void_p, # AnimationBlock *
]

_CreateRotationEntryC = _anim_dll.CreateRotationEntryC
_CreateRotationEntryC.restype = ctypes.c_void_p # Rotation *

_CreateRotationEntryC.argtypes = [
ctypes.c_uint16,
ctypes.c_float,
ctypes.c_float,
ctypes.c_float,
ctypes.c_float,
]

_DeleteRotationEntryC = _anim_dll.DeleteRotationEntryC
_DeleteRotationEntryC.restype = ctypes.c_bool
_DeleteRotationEntryC.argtypes = [
ctypes.c_void_p, # Rotation *
]

_CreateTranslationEntryC = _anim_dll.CreateTranslationEntryC
_CreateTranslationEntryC.restype = ctypes.c_void_p # Translation *

_CreateTranslationEntryC.argtypes = [
ctypes.c_uint16,
ctypes.c_double,
ctypes.c_double,
ctypes.c_double,
]

_DeleteTranslationEntryC = _anim_dll.DeleteTranslationEntryC
_DeleteTranslationEntryC.restype = ctypes.c_bool
_DeleteTranslationEntryC.argtypes = [
ctypes.c_void_p, # Translation *
]

_CreateScalarEntryC = _anim_dll.CreateScalarEntryC
_CreateScalarEntryC.restype = ctypes.c_void_p # Scalar *

_CreateScalarEntryC.argtypes = [
ctypes.c_uint16,
ctypes.c_float,
]

_DeleteScalarEntryC = _anim_dll.DeleteScalarEntryC
_DeleteScalarEntryC.restype = ctypes.c_bool
_DeleteScalarEntryC.argtypes = [
ctypes.c_void_p, # Scalar *
]

_CreatePriorityEntryC = _anim_dll.CreatePriorityEntryC
_CreatePriorityEntryC.restype = ctypes.c_void_p # Priority *

_CreatePriorityEntryC.argtypes = [
ctypes.c_uint16,
ctypes.c_uint8,
]

_DeletePriorityEntryC = _anim_dll.DeletePriorityEntryC
_DeletePriorityEntryC.restype = ctypes.c_bool
_DeletePriorityEntryC.argtypes = [
ctypes.c_void_p, # Priority *
]

_GetFrameFromTranslationEntryC = _anim_dll.GetFrameFromTranslationEntryC
_GetFrameFromTranslationEntryC.restype = ctypes.c_uint16

_GetFrameFromTranslationEntryC.argtypes = [
ctypes.c_void_p, # void *
]

_GetFrameFromRotationEntryC = _anim_dll.GetFrameFromRotationEntryC
_GetFrameFromRotationEntryC.restype = ctypes.c_uint16

_GetFrameFromRotationEntryC.argtypes = [
ctypes.c_void_p, # void *
]

_GetFrameFromScalarEntryC = _anim_dll.GetFrameFromScalarEntryC
_GetFrameFromScalarEntryC.restype = ctypes.c_uint16

_GetFrameFromScalarEntryC.argtypes = [
ctypes.c_void_p, # void *
]

_GetValueFromRotationEntryC = _anim_dll.GetValueFromRotationEntryC
_GetValueFromRotationEntryC.restype = ctypes.c_void_p # Math::Quaternion *

_GetValueFromRotationEntryC.argtypes = [
ctypes.c_void_p, # Rotation *
]

_GetValueFromTranslationEntryC = _anim_dll.GetValueFromTranslationEntryC
_GetValueFromTranslationEntryC.restype = ctypes.c_void_p # Math::Vector3D *

_GetValueFromTranslationEntryC.argtypes = [
ctypes.c_void_p, # Translation *
]

_GetValueFromScalarEntryC = _anim_dll.GetValueFromScalarEntryC
_GetValueFromScalarEntryC.restype = ctypes.c_float
_GetValueFromScalarEntryC.argtypes = [
ctypes.c_void_p, # Scalar *
]

_GetValueFromPriorityEntryC = _anim_dll.GetValueFromPriorityEntryC
_GetValueFromPriorityEntryC.restype = ctypes.c_uint8

_GetValueFromPriorityEntryC.argtypes = [
ctypes.c_void_p, # Priority *
]

_CreateAnimationSceneC = _anim_dll.CreateAnimationSceneC
_CreateAnimationSceneC.restype = ctypes.c_void_p # AnimationScene *

_CreateAnimationSceneC.argtypes = [
ctypes.c_char_p,
]

_AddRigToAnimationSceneC = _anim_dll.AddRigToAnimationSceneC
_AddRigToAnimationSceneC.restype = ctypes.c_bool
_AddRigToAnimationSceneC.argtypes = [
ctypes.c_void_p, # AnimationScene *
ctypes.c_void_p, # SkeletonRig *
ctypes.c_bool, # Utilities::StringContainer *
]

_AddAnimationToAnimationSceneC = _anim_dll.AddAnimationToAnimationSceneC
_AddAnimationToAnimationSceneC.restype = ctypes.c_bool
_AddAnimationToAnimationSceneC.argtypes = [
ctypes.c_void_p, # AnimationScene *
ctypes.c_void_p, # Animation *
ctypes.c_bool,
ctypes.c_bool, # Utilities::StringContainer *
]

_DeleteAnimationSceneC = _anim_dll.DeleteAnimationSceneC
_DeleteAnimationSceneC.restype = ctypes.c_bool
_DeleteAnimationSceneC.argtypes = [
ctypes.c_void_p, # AnimationScene *
]

_GetAnimationC = _anim_dll.GetAnimationC
_GetAnimationC.restype = ctypes.c_void_p # Animation *

_GetAnimationC.argtypes = [
ctypes.c_void_p, # AnimationScene *
ctypes.c_int,
ctypes.c_bool, # Utilities::StringContainer *
]

_GetAnimationCountC = _anim_dll.GetAnimationCountC
_GetAnimationCountC.restype = ctypes.c_size_t
_GetAnimationCountC.argtypes = [
ctypes.c_void_p, # AnimationScene *
]

_GetAnimationSceneNameC = _anim_dll.GetAnimationSceneNameC
_GetAnimationSceneNameC.restype = ctypes.c_char_p
_GetAnimationSceneNameC.argtypes = [
ctypes.c_void_p, # AnimationScene *
]

_GetSkeletonRigC = _anim_dll.GetSkeletonRigC
_GetSkeletonRigC.restype = ctypes.c_void_p # SkeletonRig *

_GetSkeletonRigC.argtypes = [
ctypes.c_void_p, # AnimationScene *
]

_HasSkeletonRigC = _anim_dll.HasSkeletonRigC
_HasSkeletonRigC.restype = ctypes.c_bool
_HasSkeletonRigC.argtypes = [
ctypes.c_void_p, # AnimationScene *
]

_GetVector2X = _anim_dll.GetVector2X
_GetVector2X.restype = ctypes.c_float
_GetVector2X.argtypes = [
ctypes.c_void_p, # Vector2 *
]

_GetVector2Y = _anim_dll.GetVector2Y
_GetVector2Y.restype = ctypes.c_float
_GetVector2Y.argtypes = [
ctypes.c_void_p, # Vector2 *
]

_GetVector2DX = _anim_dll.GetVector2DX
_GetVector2DX.restype = ctypes.c_double
_GetVector2DX.argtypes = [
ctypes.c_void_p, # Vector2D *
]

_GetVector2DY = _anim_dll.GetVector2DY
_GetVector2DY.restype = ctypes.c_double
_GetVector2DY.argtypes = [
ctypes.c_void_p, # Vector2D *
]

_GetVector3X = _anim_dll.GetVector3X
_GetVector3X.restype = ctypes.c_float
_GetVector3X.argtypes = [
ctypes.c_void_p, # Vector3 *
]

_GetVector3Y = _anim_dll.GetVector3Y
_GetVector3Y.restype = ctypes.c_float
_GetVector3Y.argtypes = [
ctypes.c_void_p, # Vector3 *
]

_GetVector3Z = _anim_dll.GetVector3Z
_GetVector3Z.restype = ctypes.c_float
_GetVector3Z.argtypes = [
ctypes.c_void_p, # Vector3 *
]

_GetVector3DX = _anim_dll.GetVector3DX
_GetVector3DX.restype = ctypes.c_double
_GetVector3DX.argtypes = [
ctypes.c_void_p, # Vector3D *
]

_GetVector3DY = _anim_dll.GetVector3DY
_GetVector3DY.restype = ctypes.c_double
_GetVector3DY.argtypes = [
ctypes.c_void_p, # Vector3D *
]

_GetVector3DZ = _anim_dll.GetVector3DZ
_GetVector3DZ.restype = ctypes.c_double
_GetVector3DZ.argtypes = [
ctypes.c_void_p, # Vector3D *
]

_GetQuaternionX = _anim_dll.GetQuaternionX
_GetQuaternionX.restype = ctypes.c_float
_GetQuaternionX.argtypes = [
ctypes.c_void_p, # Quaternion *
]

_GetQuaternionY = _anim_dll.GetQuaternionY
_GetQuaternionY.restype = ctypes.c_float
_GetQuaternionY.argtypes = [
ctypes.c_void_p, # Quaternion *
]

_GetQuaternionZ = _anim_dll.GetQuaternionZ
_GetQuaternionZ.restype = ctypes.c_float
_GetQuaternionZ.argtypes = [
ctypes.c_void_p, # Quaternion *
]

_GetQuaternionW = _anim_dll.GetQuaternionW
_GetQuaternionW.restype = ctypes.c_float
_GetQuaternionW.argtypes = [
ctypes.c_void_p, # Quaternion *
]

_RotateQuaternionByAxisAngleC = _anim_dll.RotateQuaternionByAxisAngleC
_RotateQuaternionByAxisAngleC.restype = ctypes.c_bool
_RotateQuaternionByAxisAngleC.argtypes = [
ctypes.c_void_p, # Quaternion *
ctypes.c_void_p, # Quaternion *
ctypes.c_float,
ctypes.c_float,
ctypes.c_float,
ctypes.c_float,
]

_CreateSkeletonRigC = _anim_dll.CreateSkeletonRigC
_CreateSkeletonRigC.restype = ctypes.c_void_p # SkeletonRig *

_CreateSkeletonRigC.argtypes = [
ctypes.c_char_p,
]

_DeleteSkeletonRigC = _anim_dll.DeleteSkeletonRigC
_DeleteSkeletonRigC.restype = ctypes.c_bool
_DeleteSkeletonRigC.argtypes = [
ctypes.c_void_p, # SkeletonRig *
]

_AddBoneToSkeletonRigC = _anim_dll.AddBoneToSkeletonRigC
_AddBoneToSkeletonRigC.restype = ctypes.c_bool
_AddBoneToSkeletonRigC.argtypes = [
ctypes.c_void_p, # SkeletonRig *
ctypes.c_float,
ctypes.c_float,
ctypes.c_float,
ctypes.c_float,
ctypes.c_float,
ctypes.c_float,
ctypes.c_float,
ctypes.c_char_p,
ctypes.c_int,
ctypes.c_bool,
ctypes.c_void_p, # Utilities::StringContainer *
]

_SetBoneTypeC = _anim_dll.SetBoneTypeC
_SetBoneTypeC.restype = ctypes.c_bool
_SetBoneTypeC.argtypes = [
ctypes.c_void_p, # SkeletonBone *
ctypes.c_uint32,
]

_SetBoneTypeFromStringC = _anim_dll.SetBoneTypeFromStringC
_SetBoneTypeFromStringC.restype = ctypes.c_bool
_SetBoneTypeFromStringC.argtypes = [
ctypes.c_void_p, # SkeletonBone *
ctypes.c_char_p,
]

_GetBoneTypeC = _anim_dll.GetBoneTypeC
_GetBoneTypeC.restype = ctypes.c_uint32

_GetBoneTypeC.argtypes = [
ctypes.c_void_p, # SkeletonBone *
]

_GetBoneTypeAsStringC = _anim_dll.GetBoneTypeAsStringC
_GetBoneTypeAsStringC.restype = ctypes.c_char_p
_GetBoneTypeAsStringC.argtypes = [
ctypes.c_void_p, # SkeletonBone *
]

_SetTwistBonePropertiesC = _anim_dll.SetTwistBonePropertiesC
_SetTwistBonePropertiesC.restype = ctypes.c_bool
_SetTwistBonePropertiesC.argtypes = [
ctypes.c_void_p, # SkeletonBone *
ctypes.c_bool,
ctypes.c_int32,
ctypes.c_float,
ctypes.c_void_p, # Utilities::StringContainer *
]

_GetTwistBoneDriverIndexC = _anim_dll.GetTwistBoneDriverIndexC
_GetTwistBoneDriverIndexC.restype = ctypes.c_int
_GetTwistBoneDriverIndexC.argtypes = [
ctypes.c_void_p, # SkeletonBone *
ctypes.c_bool, # Utilities::StringContainer *
]

_GetTwistBoneDriverWeightC = _anim_dll.GetTwistBoneDriverWeightC
_GetTwistBoneDriverWeightC.restype = ctypes.c_float
_GetTwistBoneDriverWeightC.argtypes = [
ctypes.c_void_p, # SkeletonBone *
ctypes.c_bool, # Utilities::StringContainer *
]

_SetMirrorIndexC = _anim_dll.SetMirrorIndexC
_SetMirrorIndexC.restype = ctypes.c_int
_SetMirrorIndexC.argtypes = [
ctypes.c_void_p, # SkeletonBone *
ctypes.c_int,
]

_GetMirrorIndexC = _anim_dll.GetMirrorIndexC
_GetMirrorIndexC.restype = ctypes.c_int
_GetMirrorIndexC.argtypes = [
ctypes.c_void_p, # SkeletonBone *
]

_CreateBoneMirrorPairC = _anim_dll.CreateBoneMirrorPairC
_CreateBoneMirrorPairC.restype = ctypes.c_bool
_CreateBoneMirrorPairC.argtypes = [
ctypes.c_void_p, # SkeletonRig *
ctypes.c_int,
ctypes.c_int,
]

_ResetAllBoneMirrorsC = _anim_dll.ResetAllBoneMirrorsC
_ResetAllBoneMirrorsC.restype = ctypes.c_bool
_ResetAllBoneMirrorsC.argtypes = [
ctypes.c_void_p, # SkeletonRig *
]

_VerifyExclusiveBoneMirrorsC = _anim_dll.VerifyExclusiveBoneMirrorsC
_VerifyExclusiveBoneMirrorsC.restype = ctypes.c_bool
_VerifyExclusiveBoneMirrorsC.argtypes = [
ctypes.c_void_p, # SkeletonRig *
]

_GetSkeletonRigBoneCountC = _anim_dll.GetSkeletonRigBoneCountC
_GetSkeletonRigBoneCountC.restype = ctypes.c_size_t
_GetSkeletonRigBoneCountC.argtypes = [
ctypes.c_void_p, # SkeletonRig *
]

_GetSkeletonRigAnimatedBoneCountC = _anim_dll.GetSkeletonRigAnimatedBoneCountC
_GetSkeletonRigAnimatedBoneCountC.restype = ctypes.c_size_t
_GetSkeletonRigAnimatedBoneCountC.argtypes = [
ctypes.c_void_p, # SkeletonRig *
]

_GetSkeletonRigNameC = _anim_dll.GetSkeletonRigNameC
_GetSkeletonRigNameC.restype = ctypes.c_char_p
_GetSkeletonRigNameC.argtypes = [
ctypes.c_void_p, # SkeletonRig *
]

_GetSkeletonBoneC = _anim_dll.GetSkeletonBoneC
_GetSkeletonBoneC.restype = ctypes.c_void_p # SkeletonBone *

_GetSkeletonBoneC.argtypes = [
ctypes.c_void_p, # SkeletonRig *
ctypes.c_int,
ctypes.c_bool, # Utilities::StringContainer *
]

_GetSkeletonBoneNameC = _anim_dll.GetSkeletonBoneNameC
_GetSkeletonBoneNameC.restype = ctypes.c_char_p
_GetSkeletonBoneNameC.argtypes = [
ctypes.c_void_p, # SkeletonBone *
]

_GetSkeletonBoneParentIndexC = _anim_dll.GetSkeletonBoneParentIndexC
_GetSkeletonBoneParentIndexC.restype = ctypes.c_int
_GetSkeletonBoneParentIndexC.argtypes = [
ctypes.c_void_p, # SkeletonBone *
]

_GetSkeletonBoneRotationC = _anim_dll.GetSkeletonBoneRotationC
_GetSkeletonBoneRotationC.restype = ctypes.c_void_p # CALUMI::Math::Quaternion *

_GetSkeletonBoneRotationC.argtypes = [
ctypes.c_void_p, # SkeletonBone *
ctypes.c_bool,
]

_GetSkeletonBonePositionC = _anim_dll.GetSkeletonBonePositionC
_GetSkeletonBonePositionC.restype = ctypes.c_void_p # CALUMI::Math::Vector3 *

_GetSkeletonBonePositionC.argtypes = [
ctypes.c_void_p, # SkeletonBone *
ctypes.c_bool,
]

_ValidateSkeletonRigNamesC = _anim_dll.ValidateSkeletonRigNamesC
_ValidateSkeletonRigNamesC.restype = ctypes.c_bool
_ValidateSkeletonRigNamesC.argtypes = [
ctypes.c_void_p, # SkeletonRig *
ctypes.c_bool, # Utilities::StringContainer *
]

_ValidateSkeletonRigParentIndicesC = _anim_dll.ValidateSkeletonRigParentIndicesC
_ValidateSkeletonRigParentIndicesC.restype = ctypes.c_bool
_ValidateSkeletonRigParentIndicesC.argtypes = [
ctypes.c_void_p, # SkeletonRig *
ctypes.c_bool, # Utilities::StringContainer *
]

_SaveAnimationSceneToSFBGSFormatC = _anim_dll.SaveAnimationSceneToSFBGSFormatC
_SaveAnimationSceneToSFBGSFormatC.restype = ctypes.c_bool
_SaveAnimationSceneToSFBGSFormatC.argtypes = [
ctypes.c_void_p, # UNIV::AnimationScene *
ctypes.c_void_p, # const wchar_t *
ctypes.c_bool, # Utilities::StringContainer *
]

_SaveAnimationSceneToSFBGSFormatPathOverrideC = _anim_dll.SaveAnimationSceneToSFBGSFormatPathOverrideC
_SaveAnimationSceneToSFBGSFormatPathOverrideC.restype = ctypes.c_bool
_SaveAnimationSceneToSFBGSFormatPathOverrideC.argtypes = [
ctypes.c_void_p, # UNIV::AnimationScene *
ctypes.c_void_p, # const wchar_t **
ctypes.c_size_t,
ctypes.c_bool, # Utilities::StringContainer *
]

_SaveAnimationSceneToSFBGSFormatUsingRigReferenceC = _anim_dll.SaveAnimationSceneToSFBGSFormatUsingRigReferenceC
_SaveAnimationSceneToSFBGSFormatUsingRigReferenceC.restype = ctypes.c_bool
_SaveAnimationSceneToSFBGSFormatUsingRigReferenceC.argtypes = [
ctypes.c_void_p, # UNIV::AnimationScene *
ctypes.c_void_p, # const wchar_t *
ctypes.c_void_p, # const wchar_t *
ctypes.c_bool, # Utilities::StringContainer *
]

_SaveAnimationSceneToSFBGSFormatUsingRigReferencePathOverrideC = _anim_dll.SaveAnimationSceneToSFBGSFormatUsingRigReferencePathOverrideC
_SaveAnimationSceneToSFBGSFormatUsingRigReferencePathOverrideC.restype = ctypes.c_bool
_SaveAnimationSceneToSFBGSFormatUsingRigReferencePathOverrideC.argtypes = [
ctypes.c_void_p, # UNIV::AnimationScene *
ctypes.c_void_p, # const wchar_t **
ctypes.c_size_t,
ctypes.c_void_p, # const wchar_t *
ctypes.c_bool, # Utilities::StringContainer *
]

_LoadAnimationSceneFromSFBGSFormatC = _anim_dll.LoadAnimationSceneFromSFBGSFormatC
_LoadAnimationSceneFromSFBGSFormatC.restype = ctypes.c_void_p # UNIV::AnimationScene *

_LoadAnimationSceneFromSFBGSFormatC.argtypes = [
ctypes.c_void_p, # const wchar_t **
ctypes.c_int,
ctypes.c_bool, # Utilities::StringContainer *
]

_LoadAnimationSceneFromSFBGSFormatAndSaveToJsonC = _anim_dll.LoadAnimationSceneFromSFBGSFormatAndSaveToJsonC
_LoadAnimationSceneFromSFBGSFormatAndSaveToJsonC.restype = ctypes.c_void_p # UNIV::AnimationScene *

_LoadAnimationSceneFromSFBGSFormatAndSaveToJsonC.argtypes = [
ctypes.c_void_p, # const wchar_t **
ctypes.c_int,
ctypes.c_bool, # Utilities::StringContainer *
ctypes.c_void_p, # const wchar_t *
]

_LoadSFBGSSkeletonRigFromFileC = _anim_dll.LoadSFBGSSkeletonRigFromFileC
_LoadSFBGSSkeletonRigFromFileC.restype = ctypes.c_void_p # UNIV::SkeletonRig *

_LoadSFBGSSkeletonRigFromFileC.argtypes = [
ctypes.c_void_p, # const wchar_t *
ctypes.c_bool, # Utilities::StringContainer *
]

_SFBGSRigPackage_AddPackageToSkeletonRigC = _anim_dll.SFBGSRigPackage_AddPackageToSkeletonRigC
_SFBGSRigPackage_AddPackageToSkeletonRigC.restype = ctypes.c_bool
_SFBGSRigPackage_AddPackageToSkeletonRigC.argtypes = [
ctypes.c_void_p, # UNIV::SkeletonRig *
ctypes.c_void_p, # Utilities::StringContainer *
ctypes.c_bool,
]

_SFBGSRigPackage_RemoveRigPackageFromSkeletonRigC = _anim_dll.SFBGSRigPackage_RemoveRigPackageFromSkeletonRigC
_SFBGSRigPackage_RemoveRigPackageFromSkeletonRigC.restype = ctypes.c_bool
_SFBGSRigPackage_RemoveRigPackageFromSkeletonRigC.argtypes = [
ctypes.c_void_p, # UNIV::SkeletonRig *
ctypes.c_bool, # Utilities::StringContainer *
]

_SFBGSRigPackage_BoneIsMappedC = _anim_dll.SFBGSRigPackage_BoneIsMappedC
_SFBGSRigPackage_BoneIsMappedC.restype = ctypes.c_bool
_SFBGSRigPackage_BoneIsMappedC.argtypes = [
ctypes.c_void_p, # UNIV::SkeletonRig *
ctypes.c_char_p,
]

_SFBGSRigPackage_KeyIsMappedC = _anim_dll.SFBGSRigPackage_KeyIsMappedC
_SFBGSRigPackage_KeyIsMappedC.restype = ctypes.c_bool
_SFBGSRigPackage_KeyIsMappedC.argtypes = [
ctypes.c_void_p, # UNIV::SkeletonRig *
ctypes.c_uint8,
]

_SFBGSRigPackage_AddBoneNameToMapC = _anim_dll.SFBGSRigPackage_AddBoneNameToMapC
_SFBGSRigPackage_AddBoneNameToMapC.restype = ctypes.c_bool
_SFBGSRigPackage_AddBoneNameToMapC.argtypes = [
ctypes.c_void_p, # UNIV::SkeletonRig *
ctypes.c_uint8,
ctypes.c_char_p,
ctypes.c_void_p, # Utilities::StringContainer *
ctypes.c_bool,
]

_SFBGSRigPackage_AddBoneToMapC = _anim_dll.SFBGSRigPackage_AddBoneToMapC
_SFBGSRigPackage_AddBoneToMapC.restype = ctypes.c_bool
_SFBGSRigPackage_AddBoneToMapC.argtypes = [
ctypes.c_void_p, # UNIV::SkeletonRig *
ctypes.c_uint8,
ctypes.c_void_p, # UNIV::SkeletonBone *
ctypes.c_void_p, # Utilities::StringContainer *
ctypes.c_bool,
]

_SFBGSRigPackage_RemoveBoneFromMapUsingKeyC = _anim_dll.SFBGSRigPackage_RemoveBoneFromMapUsingKeyC
_SFBGSRigPackage_RemoveBoneFromMapUsingKeyC.restype = ctypes.c_bool
_SFBGSRigPackage_RemoveBoneFromMapUsingKeyC.argtypes = [
ctypes.c_void_p, # UNIV::SkeletonRig *
ctypes.c_uint8,
]

_SFBGSRigPackage_RemoveBoneFromMapUsingNameC = _anim_dll.SFBGSRigPackage_RemoveBoneFromMapUsingNameC
_SFBGSRigPackage_RemoveBoneFromMapUsingNameC.restype = ctypes.c_bool
_SFBGSRigPackage_RemoveBoneFromMapUsingNameC.argtypes = [
ctypes.c_void_p, # UNIV::SkeletonRig *
ctypes.c_char_p,
]

_SFBGSRigPackage_GetBoneKeyC = _anim_dll.SFBGSRigPackage_GetBoneKeyC
_SFBGSRigPackage_GetBoneKeyC.restype = ctypes.c_uint8

_SFBGSRigPackage_GetBoneKeyC.argtypes = [
ctypes.c_void_p, # UNIV::SkeletonRig *
ctypes.c_char_p,
]

_SFBGSRigPackage_GetBoneNameFromKeyC = _anim_dll.SFBGSRigPackage_GetBoneNameFromKeyC
_SFBGSRigPackage_GetBoneNameFromKeyC.restype = ctypes.c_char_p
_SFBGSRigPackage_GetBoneNameFromKeyC.argtypes = [
ctypes.c_void_p, # UNIV::SkeletonRig *
ctypes.c_uint8,
]

_SFBGSRigPackage_SetMannequinC = _anim_dll.SFBGSRigPackage_SetMannequinC
_SFBGSRigPackage_SetMannequinC.restype = ctypes.c_bool
_SFBGSRigPackage_SetMannequinC.argtypes = [
ctypes.c_void_p, # UNIV::SkeletonRig *
ctypes.c_bool,
]

_SFBGSRigPackage_GetRigMapSize = _anim_dll.SFBGSRigPackage_GetRigMapSize
_SFBGSRigPackage_GetRigMapSize.restype = ctypes.c_size_t
_SFBGSRigPackage_GetRigMapSize.argtypes = [

]

_SFBGSRigPackage_SetPrecisionToDefaultC = _anim_dll.SFBGSRigPackage_SetPrecisionToDefaultC
_SFBGSRigPackage_SetPrecisionToDefaultC.restype = ctypes.c_void_p # void

_SFBGSRigPackage_SetPrecisionToDefaultC.argtypes = [
ctypes.c_void_p, # UNIV::SkeletonRig *
]

_SFBGSRigPackage_SetPrecisionToFirstPersonC = _anim_dll.SFBGSRigPackage_SetPrecisionToFirstPersonC
_SFBGSRigPackage_SetPrecisionToFirstPersonC.restype = ctypes.c_void_p # void

_SFBGSRigPackage_SetPrecisionToFirstPersonC.argtypes = [
ctypes.c_void_p, # UNIV::SkeletonRig *
]

_SFBGSRigPackage_SetPrecisionToShipValuesC = _anim_dll.SFBGSRigPackage_SetPrecisionToShipValuesC
_SFBGSRigPackage_SetPrecisionToShipValuesC.restype = ctypes.c_void_p # void

_SFBGSRigPackage_SetPrecisionToShipValuesC.argtypes = [
ctypes.c_void_p, # UNIV::SkeletonRig *
]

_SFBGSRigPackage_SetPrecisionToCustomC = _anim_dll.SFBGSRigPackage_SetPrecisionToCustomC
_SFBGSRigPackage_SetPrecisionToCustomC.restype = ctypes.c_void_p # void

_SFBGSRigPackage_SetPrecisionToCustomC.argtypes = [
ctypes.c_void_p, # UNIV::SkeletonRig *
ctypes.c_float,
ctypes.c_float,
]
_SaveAnimationToSFBGSFormatWithExistingRigDirectC = _anim_dll.SaveAnimationToSFBGSFormatWithExistingRigDirectC
_SaveAnimationToSFBGSFormatWithExistingRigDirectC.restype = ctypes.c_bool
_SaveAnimationToSFBGSFormatWithExistingRigDirectC.argtypes = [
ctypes.c_void_p, # UNIV::Animation *
ctypes.c_wchar_p, # const wchar_t * filePath
ctypes.c_wchar_p, # const wchar_t * rigPath
ctypes.c_bool, # StringContainer errorMsg
]

_SFBGSRigPackage_GetPrecisionTypeC = _anim_dll.SFBGSRigPackage_GetPrecisionTypeC
_SFBGSRigPackage_GetPrecisionTypeC.restype = ctypes.c_uint8
_SFBGSRigPackage_GetPrecisionTypeC.argtypes = [
    ctypes.c_void_p # UNIV::SkeletonRig* rig
]

_SFBGSRigPackage_GetHighPrecisionValueC = _anim_dll.SFBGSRigPackage_GetHighPrecisionValueC
_SFBGSRigPackage_GetHighPrecisionValueC.restype = ctypes.c_float
_SFBGSRigPackage_GetHighPrecisionValueC.argtypes = [
    ctypes.c_void_p # UNIV::SkeletonRig* rig
]

_SFBGSRigPackage_GetLowPrecisionValueC = _anim_dll.SFBGSRigPackage_GetLowPrecisionValueC
_SFBGSRigPackage_GetLowPrecisionValueC.restype = ctypes.c_float
_SFBGSRigPackage_GetLowPrecisionValueC.argtypes = [
    ctypes.c_void_p # UNIV::SkeletonRig* rig
]

_SFBGSRigPackage_IsMannequinC = _anim_dll.SFBGSRigPackage_IsMannequinC
_SFBGSRigPackage_IsMannequinC.restype = ctypes.c_float
_SFBGSRigPackage_IsMannequinC.argtypes = [
    ctypes.c_void_p # UNIV::SkeletonRig* rig
]

_SaveSkeletonRigToSFBGSFormatDirectC = _anim_dll.SaveSkeletonRigToSFBGSFormatDirectC
_SaveSkeletonRigToSFBGSFormatDirectC.restype = ctypes.c_bool
_SaveSkeletonRigToSFBGSFormatDirectC.argtypes = [
    ctypes.c_void_p, # UNIV::SkeletonRig* rig
    ctypes.c_wchar_p, # const wchar_t* filePath
    ctypes.c_void_p, # error message
]

_CreateStringContainerC = _anim_dll.CreateStringContainerC
_CreateStringContainerC.restype = ctypes.c_void_p
_CreateStringContainerC.argtypes = []

_GetStringFromContainerC = _anim_dll.GetStringFromContainerC
_GetStringFromContainerC.restype = ctypes.c_char_p
_GetStringFromContainerC.argtypes = [ctypes.c_void_p]

_ExecuteRDPReduction_ScalarC = _anim_dll.ExecuteRDPReduction_ScalarC
_ExecuteRDPReduction_ScalarC.restype = ctypes.c_void_p
_ExecuteRDPReduction_ScalarC.argtypes = [
    ctypes.c_void_p, # AnimationBlock*
    ctypes.c_float # Tolerance
]

_ExecuteRDPReduction_TranslationC = _anim_dll.ExecuteRDPReduction_TranslationC
_ExecuteRDPReduction_TranslationC.restype = ctypes.c_void_p
_ExecuteRDPReduction_TranslationC.argtypes = [
    ctypes.c_void_p, # AnimationBlock*
    ctypes.c_float # Tolerance
]

_ExecuteRDPReduction_RotationC = _anim_dll.ExecuteRDPReduction_RotationC
_ExecuteRDPReduction_RotationC.restype = ctypes.c_void_p
_ExecuteRDPReduction_RotationC.argtypes = [
    ctypes.c_void_p, # AnimationBlock*
    ctypes.c_float # Tolerance
]

