import ctypes
import os

_anim_dll = ctypes.CDLL(os.path.join(os.path.dirname(os.path.dirname(__file__)),'CALUMI.Animation.dll'))
PATH_FOR_IMPORT_JSON = "C:\\General Files\\Git\\AnimScript\\AnimStarfieldMeshConverter_repo\\scripts\\tool_export_mesh\\ExportedJSONs\\LastFile.json"

def _list_to_wchar_arr(python_list):
    arr = (ctypes.c_wchar_p * len(python_list))()
    arr[:] = python_list
    return arr

#_CreateVector2C = _anim_dll.CreateVector2C
#_CreateVector2C.restype = ctypes.c_void_p # CALUMI::Math::Vector2 *
#
#_CreateVector2C.argtypes = [
#ctypes.c_float,
#ctypes.c_float,
#]

_GetVector2XC = _anim_dll.GetVector2XC
_GetVector2XC.restype = ctypes.c_float
_GetVector2XC.argtypes = [
ctypes.c_void_p, # CALUMI::Math::Vector2 *
]

_GetVector2YC = _anim_dll.GetVector2YC
_GetVector2YC.restype = ctypes.c_float
_GetVector2YC.argtypes = [
ctypes.c_void_p, # CALUMI::Math::Vector2 *
]

_DeleteVector2C = _anim_dll.DeleteVector2C
_DeleteVector2C.restype = ctypes.c_int
_DeleteVector2C.argtypes = [
ctypes.c_void_p, # CALUMI::Math::Vector2 **
]

_CreateVector2DC = _anim_dll.CreateVector2DC
_CreateVector2DC.restype = ctypes.c_void_p # CALUMI::Math::Vector2D *

_CreateVector2DC.argtypes = [
ctypes.c_float,
ctypes.c_float,
]

_GetVector2DXC = _anim_dll.GetVector2DXC
_GetVector2DXC.restype = ctypes.c_double
_GetVector2DXC.argtypes = [
ctypes.c_void_p, # CALUMI::Math::Vector2D *
]

_GetVector2DYC = _anim_dll.GetVector2DYC
_GetVector2DYC.restype = ctypes.c_double
_GetVector2DYC.argtypes = [
ctypes.c_void_p, # CALUMI::Math::Vector2D *
]

_DeleteVector2DC = _anim_dll.DeleteVector2DC
_DeleteVector2DC.restype = ctypes.c_int
_DeleteVector2DC.argtypes = [
ctypes.c_void_p, # CALUMI::Math::Vector2D **
]

_CreateVector3C = _anim_dll.CreateVector3C
_CreateVector3C.restype = ctypes.c_void_p # CALUMI::Math::Vector3 *

_CreateVector3C.argtypes = [
ctypes.c_float,
ctypes.c_float,
ctypes.c_float,
]

_GetVector3XC = _anim_dll.GetVector3XC
_GetVector3XC.restype = ctypes.c_float
_GetVector3XC.argtypes = [
ctypes.c_void_p, # CALUMI::Math::Vector3 *
]

_GetVector3YC = _anim_dll.GetVector3YC
_GetVector3YC.restype = ctypes.c_float
_GetVector3YC.argtypes = [
ctypes.c_void_p, # CALUMI::Math::Vector3 *
]

_GetVector3ZC = _anim_dll.GetVector3ZC
_GetVector3ZC.restype = ctypes.c_float
_GetVector3ZC.argtypes = [
ctypes.c_void_p, # CALUMI::Math::Vector3 *
]

_DeleteVector3C = _anim_dll.DeleteVector3C
_DeleteVector3C.restype = ctypes.c_int
_DeleteVector3C.argtypes = [
ctypes.c_void_p, # CALUMI::Math::Vector3 **
]

_CreateVector3DC = _anim_dll.CreateVector3DC
_CreateVector3DC.restype = ctypes.c_void_p # CALUMI::Math::Vector3D *

_CreateVector3DC.argtypes = [
ctypes.c_double,
ctypes.c_double,
ctypes.c_double,
]

_GetVector3DXC = _anim_dll.GetVector3DXC
_GetVector3DXC.restype = ctypes.c_double
_GetVector3DXC.argtypes = [
ctypes.c_void_p, # CALUMI::Math::Vector3D *
]

_GetVector3DYC = _anim_dll.GetVector3DYC
_GetVector3DYC.restype = ctypes.c_double
_GetVector3DYC.argtypes = [
ctypes.c_void_p, # CALUMI::Math::Vector3D *
]

_GetVector3DZC = _anim_dll.GetVector3DZC
_GetVector3DZC.restype = ctypes.c_double
_GetVector3DZC.argtypes = [
ctypes.c_void_p, # CALUMI::Math::Vector3D *
]

_DeleteVector3DC = _anim_dll.DeleteVector3DC
_DeleteVector3DC.restype = ctypes.c_int
_DeleteVector3DC.argtypes = [
ctypes.c_void_p, # CALUMI::Math::Vector3D **
]

_CreateTransformC = _anim_dll.CreateTransformC
_CreateTransformC.restype = ctypes.c_void_p # CALUMI::Math::Transform *

_CreateTransformC.argtypes = [

]

_SetTransformFromReferenceC = _anim_dll.SetTransformFromReferenceC
_SetTransformFromReferenceC.restype = ctypes.c_int
_SetTransformFromReferenceC.argtypes = [
ctypes.c_void_p, # CALUMI::Math::Transform *
ctypes.c_void_p, # CALUMI::Math::Transform *
]

_GetLocalTransformC = _anim_dll.GetLocalTransformC
_GetLocalTransformC.restype = ctypes.c_void_p # CALUMI::Math::Transform *

_GetLocalTransformC.argtypes = [
ctypes.c_void_p, # CALUMI::Math::Transform *
ctypes.c_void_p, # CALUMI::Math::Transform *
]

_GetGlobalTransformC = _anim_dll.GetGlobalTransformC
_GetGlobalTransformC.restype = ctypes.c_void_p # CALUMI::Math::Transform *

_GetGlobalTransformC.argtypes = [
ctypes.c_void_p, # CALUMI::Math::Transform *
ctypes.c_void_p, # CALUMI::Math::Transform *
]

_SetTransformPositionC = _anim_dll.SetTransformPositionC
_SetTransformPositionC.restype = ctypes.c_int
_SetTransformPositionC.argtypes = [
ctypes.c_void_p, # CALUMI::Math::Transform *
ctypes.c_float,
ctypes.c_float,
ctypes.c_float,
]

_SetTransformPositionFromReferenceC = _anim_dll.SetTransformPositionFromReferenceC
_SetTransformPositionFromReferenceC.restype = ctypes.c_int
_SetTransformPositionFromReferenceC.argtypes = [
ctypes.c_void_p, # CALUMI::Math::Transform *
ctypes.c_void_p, # CALUMI::Math::Vector3 *
]

_SetTransformRotationC = _anim_dll.SetTransformRotationC
_SetTransformRotationC.restype = ctypes.c_int
_SetTransformRotationC.argtypes = [
ctypes.c_void_p, # CALUMI::Math::Transform *
ctypes.c_float,
ctypes.c_float,
ctypes.c_float,
ctypes.c_float,
]

_SetTransformEulerRotationC = _anim_dll.SetTransformEulerRotationC
_SetTransformEulerRotationC.restype = ctypes.c_int
_SetTransformEulerRotationC.argtypes = [
ctypes.c_void_p, # CALUMI::Math::Transform *
ctypes.c_float,
ctypes.c_float,
ctypes.c_float,
ctypes.c_int,
]

_SetTransformRotationFromReferenceC = _anim_dll.SetTransformRotationFromReferenceC
_SetTransformRotationFromReferenceC.restype = ctypes.c_int
_SetTransformRotationFromReferenceC.argtypes = [
ctypes.c_void_p, # CALUMI::Math::Transform *
ctypes.c_void_p, # CALUMI::Math::Quaternion *
]

_GetTransformEulerRotationC = _anim_dll.GetTransformEulerRotationC
_GetTransformEulerRotationC.restype = ctypes.c_int
_GetTransformEulerRotationC.argtypes = [
ctypes.c_void_p, # CALUMI::Math::Transform *
ctypes.c_void_p, # float *
ctypes.c_void_p, # float *
ctypes.c_void_p, # float *
ctypes.c_int,
]

_GetTransformPositionC = _anim_dll.GetTransformPositionC
_GetTransformPositionC.restype = ctypes.c_void_p # CALUMI::Math::Vector3 *

_GetTransformPositionC.argtypes = [
ctypes.c_void_p, # CALUMI::Math::Transform *
]

_GetTransformPositionXC = _anim_dll.GetTransformPositionXC
_GetTransformPositionXC.restype = ctypes.c_float
_GetTransformPositionXC.argtypes = [
ctypes.c_void_p, # CALUMI::Math::Transform *
]

_GetTransformPositionYC = _anim_dll.GetTransformPositionYC
_GetTransformPositionYC.restype = ctypes.c_float
_GetTransformPositionYC.argtypes = [
ctypes.c_void_p, # CALUMI::Math::Transform *
]

_GetTransformPositionZC = _anim_dll.GetTransformPositionZC
_GetTransformPositionZC.restype = ctypes.c_float
_GetTransformPositionZC.argtypes = [
ctypes.c_void_p, # CALUMI::Math::Transform *
]

_GetTransformRotationC = _anim_dll.GetTransformRotationC
_GetTransformRotationC.restype = ctypes.c_void_p # CALUMI::Math::Quaternion *

_GetTransformRotationC.argtypes = [
ctypes.c_void_p, # CALUMI::Math::Transform *
]

_GetTransformRotationXC = _anim_dll.GetTransformRotationXC
_GetTransformRotationXC.restype = ctypes.c_float
_GetTransformRotationXC.argtypes = [
ctypes.c_void_p, # CALUMI::Math::Transform *
]

_GetTransformRotationYC = _anim_dll.GetTransformRotationYC
_GetTransformRotationYC.restype = ctypes.c_float
_GetTransformRotationYC.argtypes = [
ctypes.c_void_p, # CALUMI::Math::Transform *
]

_GetTransformRotationZC = _anim_dll.GetTransformRotationZC
_GetTransformRotationZC.restype = ctypes.c_float
_GetTransformRotationZC.argtypes = [
ctypes.c_void_p, # CALUMI::Math::Transform *
]

_GetTransformRotationWC = _anim_dll.GetTransformRotationWC
_GetTransformRotationWC.restype = ctypes.c_float
_GetTransformRotationWC.argtypes = [
ctypes.c_void_p, # CALUMI::Math::Transform *
]

_DeleteTransformC = _anim_dll.DeleteTransformC
_DeleteTransformC.restype = ctypes.c_int
_DeleteTransformC.argtypes = [
ctypes.c_void_p, # CALUMI::Math::Transform **
]

_CreateQuaternionC = _anim_dll.CreateQuaternionC
_CreateQuaternionC.restype = ctypes.c_void_p # CALUMI::Math::Quaternion *

_CreateQuaternionC.argtypes = [
ctypes.c_float,
ctypes.c_float,
ctypes.c_float,
ctypes.c_float,
]

#_CreateQuaternionFromEulerC = _anim_dll.CreateQuaternionFromEulerC
#_CreateQuaternionFromEulerC.restype = ctypes.c_void_p # CALUMI::Math::Quaternion *
#
#_CreateQuaternionFromEulerC.argtypes = [
#ctypes.c_float,
#ctypes.c_float,
#ctypes.c_float,
#ctypes.c_int,
#]

_GetQuaternionXC = _anim_dll.GetQuaternionXC
_GetQuaternionXC.restype = ctypes.c_float
_GetQuaternionXC.argtypes = [
ctypes.c_void_p, # CALUMI::Math::Quaternion *
]

_GetQuaternionYC = _anim_dll.GetQuaternionYC
_GetQuaternionYC.restype = ctypes.c_float
_GetQuaternionYC.argtypes = [
ctypes.c_void_p, # CALUMI::Math::Quaternion *
]

_GetQuaternionZC = _anim_dll.GetQuaternionZC
_GetQuaternionZC.restype = ctypes.c_float
_GetQuaternionZC.argtypes = [
ctypes.c_void_p, # CALUMI::Math::Quaternion *
]

_GetQuaternionWC = _anim_dll.GetQuaternionWC
_GetQuaternionWC.restype = ctypes.c_float
_GetQuaternionWC.argtypes = [
ctypes.c_void_p, # CALUMI::Math::Quaternion *
]

_GetQuaternionToEulerC = _anim_dll.GetQuaternionToEulerC
_GetQuaternionToEulerC.restype = ctypes.c_int
_GetQuaternionToEulerC.argtypes = [
ctypes.c_void_p, # CALUMI::Math::Quaternion *
ctypes.c_int,
ctypes.c_void_p, # float *
ctypes.c_void_p, # float *
ctypes.c_void_p, # float *
]

_RotateQuaternionByAxisAngleC = _anim_dll.RotateQuaternionByAxisAngleC
_RotateQuaternionByAxisAngleC.restype = ctypes.c_int
_RotateQuaternionByAxisAngleC.argtypes = [
ctypes.c_void_p, # CALUMI::Math::Quaternion *
ctypes.c_void_p, # CALUMI::Math::Quaternion *
ctypes.c_float,
ctypes.c_float,
ctypes.c_float,
ctypes.c_float,
]

_RotateQuaternionByQuaternionC = _anim_dll.RotateQuaternionByQuaternionC
_RotateQuaternionByQuaternionC.restype = ctypes.c_int
_RotateQuaternionByQuaternionC.argtypes = [
ctypes.c_void_p, # CALUMI::Math::Quaternion *
ctypes.c_void_p, # CALUMI::Math::Quaternion *
ctypes.c_void_p, # CALUMI::Math::Quaternion *
]

_GetQuaternionOffsetC = _anim_dll.GetQuaternionOffsetC
_GetQuaternionOffsetC.restype = ctypes.c_int
_GetQuaternionOffsetC.argtypes = [
ctypes.c_void_p, # CALUMI::Math::Quaternion *
ctypes.c_void_p, # CALUMI::Math::Quaternion *
ctypes.c_void_p, # CALUMI::Math::Quaternion *
]

_DeleteQuaternionC = _anim_dll.DeleteQuaternionC
_DeleteQuaternionC.restype = ctypes.c_int
_DeleteQuaternionC.argtypes = [
ctypes.c_void_p, # CALUMI::Math::Quaternion **
]

_SaveAnimationSceneToSFBGSFormatPathOverrideC = _anim_dll.SaveAnimationSceneToSFBGSFormatPathOverrideC
_SaveAnimationSceneToSFBGSFormatPathOverrideC.restype = ctypes.c_int
_SaveAnimationSceneToSFBGSFormatPathOverrideC.argtypes = [
ctypes.c_void_p, # CALUMI::UNIV::AnimationScene *
ctypes.c_void_p, # const wchar_t **
ctypes.c_uint64,
]

_SaveAnimationSceneToSFBGSFormatUsingRigReferencePathOverrideC = _anim_dll.SaveAnimationSceneToSFBGSFormatUsingRigReferencePathOverrideC
_SaveAnimationSceneToSFBGSFormatUsingRigReferencePathOverrideC.restype = ctypes.c_int
_SaveAnimationSceneToSFBGSFormatUsingRigReferencePathOverrideC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::AnimationScene *
ctypes.c_void_p, # const wchar_t **
ctypes.c_uint64,
ctypes.c_void_p, # const wchar_t *
]

_LoadAnimationSceneFromSFBGSFormatC = _anim_dll.LoadAnimationSceneFromSFBGSFormatC
_LoadAnimationSceneFromSFBGSFormatC.restype = ctypes.c_void_p # CALUMI::UNIV::AnimationScene *

_LoadAnimationSceneFromSFBGSFormatC.argtypes = [
ctypes.c_void_p, # const wchar_t **
ctypes.c_int,
]

_LoadSFBGSSkeletonRigFromFileC = _anim_dll.LoadSFBGSSkeletonRigFromFileC
_LoadSFBGSSkeletonRigFromFileC.restype = ctypes.c_void_p # CALUMI::UNIV::SkeletonRig *

_LoadSFBGSSkeletonRigFromFileC.argtypes = [
ctypes.c_wchar_p, # const wchar_t *
]

_SaveAnimationToSFBGSFormatDirectC = _anim_dll.SaveAnimationToSFBGSFormatDirectC
_SaveAnimationToSFBGSFormatDirectC.restype = ctypes.c_int
_SaveAnimationToSFBGSFormatDirectC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::Animation *
ctypes.c_void_p, # const wchar_t *
ctypes.c_void_p, # const CALUMI::UNIV::SkeletonRig *
]

_SaveAnimationToSFBGSFormatWithExistingRigDirectC = _anim_dll.SaveAnimationToSFBGSFormatWithExistingRigDirectC
_SaveAnimationToSFBGSFormatWithExistingRigDirectC.restype = ctypes.c_int
_SaveAnimationToSFBGSFormatWithExistingRigDirectC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::Animation *
ctypes.c_void_p, # const wchar_t *
ctypes.c_void_p, # const wchar_t *
]

_SaveSkeletonRigToSFBGSFormatDirectC = _anim_dll.SaveSkeletonRigToSFBGSFormatDirectC
_SaveSkeletonRigToSFBGSFormatDirectC.restype = ctypes.c_int
_SaveSkeletonRigToSFBGSFormatDirectC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::SkeletonRig *
ctypes.c_void_p, # const wchar_t *
]

_CreateAnimationSceneC = _anim_dll.CreateAnimationSceneC
_CreateAnimationSceneC.restype = ctypes.c_void_p # CALUMI::UNIV::AnimationScene *

_CreateAnimationSceneC.argtypes = [
ctypes.c_char_p,
]

_AddRigToAnimationSceneC = _anim_dll.AddRigToAnimationSceneC
_AddRigToAnimationSceneC.restype = ctypes.c_int
_AddRigToAnimationSceneC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::AnimationScene *
ctypes.c_void_p, # const CALUMI::UNIV::SkeletonRig *
]

_AddAnimationToAnimationSceneC = _anim_dll.AddAnimationToAnimationSceneC
_AddAnimationToAnimationSceneC.restype = ctypes.c_int
_AddAnimationToAnimationSceneC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::AnimationScene *
ctypes.c_void_p, # const CALUMI::UNIV::Animation *
ctypes.c_bool,
]

_DeleteAnimationSceneC = _anim_dll.DeleteAnimationSceneC
_DeleteAnimationSceneC.restype = ctypes.c_int
_DeleteAnimationSceneC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::AnimationScene **
]

_GetAnimationWithIndexC = _anim_dll.GetAnimationWithIndexC
_GetAnimationWithIndexC.restype = ctypes.c_void_p # CALUMI::UNIV::Animation *

_GetAnimationWithIndexC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::AnimationScene *
ctypes.c_int,
]

_GetAnimationWithNameC = _anim_dll.GetAnimationWithNameC
_GetAnimationWithNameC.restype = ctypes.c_void_p # CALUMI::UNIV::Animation *

_GetAnimationWithNameC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::AnimationScene *
ctypes.c_char_p,
]

_GetAnimationCountC = _anim_dll.GetAnimationCountC
_GetAnimationCountC.restype = ctypes.c_uint64
_GetAnimationCountC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::AnimationScene *
]

_GetAnimationSceneNameC = _anim_dll.GetAnimationSceneNameC
_GetAnimationSceneNameC.restype = ctypes.c_char_p
_GetAnimationSceneNameC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::AnimationScene *
]

_GetSkeletonRigC = _anim_dll.GetSkeletonRigC
_GetSkeletonRigC.restype = ctypes.c_void_p # const CALUMI::UNIV::SkeletonRig *

_GetSkeletonRigC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::AnimationScene *
]

_CreateAnimationC = _anim_dll.CreateAnimationC
_CreateAnimationC.restype = ctypes.c_void_p # CALUMI::UNIV::Animation *

_CreateAnimationC.argtypes = [
ctypes.c_char_p,
ctypes.c_void_p, # unsigned int
]

_GetAnimationBlockC = _anim_dll.GetAnimationBlockC
_GetAnimationBlockC.restype = ctypes.c_void_p # CALUMI::UNIV::AnimationBlock *

_GetAnimationBlockC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::Animation *
ctypes.c_char_p,
]

_GetAnimationBlockCountC = _anim_dll.GetAnimationBlockCountC
_GetAnimationBlockCountC.restype = ctypes.c_uint64
_GetAnimationBlockCountC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::Animation *
]

_GetAnimationTitleC = _anim_dll.GetAnimationTitleC
_GetAnimationTitleC.restype = ctypes.c_char_p
_GetAnimationTitleC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::Animation *
]

_GetFrameCountC = _anim_dll.GetFrameCountC
_GetFrameCountC.restype = ctypes.c_uint64
_GetFrameCountC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::Animation *
]

_DeleteAnimationC = _anim_dll.DeleteAnimationC
_DeleteAnimationC.restype = ctypes.c_int
_DeleteAnimationC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::Animation **
]

_AddAnimBlockToAnimationC = _anim_dll.AddAnimBlockToAnimationC
_AddAnimBlockToAnimationC.restype = ctypes.c_int
_AddAnimBlockToAnimationC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::Animation *
ctypes.c_void_p, # const CALUMI::UNIV::AnimationBlock *
ctypes.c_bool,
]

_CreateAnimBlockC = _anim_dll.CreateAnimBlockC
_CreateAnimBlockC.restype = ctypes.c_void_p # CALUMI::UNIV::AnimationBlock *

_CreateAnimBlockC.argtypes = [
ctypes.c_char_p,
]

_DeleteAnimationBlockC = _anim_dll.DeleteAnimationBlockC
_DeleteAnimationBlockC.restype = ctypes.c_int
_DeleteAnimationBlockC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::AnimationBlock **
]

_GetAnimBlockBoneNameC = _anim_dll.GetAnimBlockBoneNameC
_GetAnimBlockBoneNameC.restype = ctypes.c_char_p
_GetAnimBlockBoneNameC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::AnimationBlock *
]

_GetLastFrameInAnimBlockC = _anim_dll.GetLastFrameInAnimBlockC
_GetLastFrameInAnimBlockC.restype = ctypes.c_uint

_GetLastFrameInAnimBlockC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::AnimationBlock *
]

_AddRotationSqToAnimBlockC = _anim_dll.AddRotationSqToAnimBlockC
_AddRotationSqToAnimBlockC.restype = ctypes.c_uint

_AddRotationSqToAnimBlockC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::AnimationBlock *
ctypes.c_void_p, # const CALUMI::UNIV::RotationFrame *
ctypes.c_void_p, # unsigned int
ctypes.c_bool,
]

_GetRotationSqArrayC = _anim_dll.GetRotationSqArrayC
_GetRotationSqArrayC.restype = ctypes.c_void_p # CALUMI::UNIV::RotationFrame *

_GetRotationSqArrayC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::AnimationBlock *
]

_GetRotationFromSqC = _anim_dll.GetRotationFromSqC
_GetRotationFromSqC.restype = ctypes.c_void_p # CALUMI::UNIV::RotationFrame *

_GetRotationFromSqC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::AnimationBlock *
ctypes.c_int,
]

_GetRotationSqSizeC = _anim_dll.GetRotationSqSizeC
_GetRotationSqSizeC.restype = ctypes.c_uint64
_GetRotationSqSizeC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::AnimationBlock *
]

_AddTranslationSqToAnimBlockC = _anim_dll.AddTranslationSqToAnimBlockC
_AddTranslationSqToAnimBlockC.restype = ctypes.c_uint

_AddTranslationSqToAnimBlockC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::AnimationBlock *
ctypes.c_void_p, # const CALUMI::UNIV::TranslationFrame *
ctypes.c_void_p, # unsigned int
ctypes.c_bool,
]

_GetTranslationSqArrayC = _anim_dll.GetTranslationSqArrayC
_GetTranslationSqArrayC.restype = ctypes.c_void_p # CALUMI::UNIV::TranslationFrame *

_GetTranslationSqArrayC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::AnimationBlock *
]

_GetTranslationFromSqC = _anim_dll.GetTranslationFromSqC
_GetTranslationFromSqC.restype = ctypes.c_void_p # CALUMI::UNIV::TranslationFrame *

_GetTranslationFromSqC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::AnimationBlock *
ctypes.c_int,
]

_GetTranslationSqSizeC = _anim_dll.GetTranslationSqSizeC
_GetTranslationSqSizeC.restype = ctypes.c_uint64
_GetTranslationSqSizeC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::AnimationBlock *
]

_AddScalarSqToAnimBlockC = _anim_dll.AddScalarSqToAnimBlockC
_AddScalarSqToAnimBlockC.restype = ctypes.c_uint

_AddScalarSqToAnimBlockC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::AnimationBlock *
ctypes.c_void_p, # const CALUMI::UNIV::ScalarFrame *
ctypes.c_void_p, # unsigned int
ctypes.c_bool,
]

_GetScalarSqArrayC = _anim_dll.GetScalarSqArrayC
_GetScalarSqArrayC.restype = ctypes.c_void_p # CALUMI::UNIV::ScalarFrame *

_GetScalarSqArrayC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::AnimationBlock *
]

_GetScalarFromSqC = _anim_dll.GetScalarFromSqC
_GetScalarFromSqC.restype = ctypes.c_void_p # CALUMI::UNIV::ScalarFrame *

_GetScalarFromSqC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::AnimationBlock *
ctypes.c_int,
]

_GetScalarSqSizeC = _anim_dll.GetScalarSqSizeC
_GetScalarSqSizeC.restype = ctypes.c_uint64
_GetScalarSqSizeC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::AnimationBlock *
]

_AddPrioritySqToAnimBlockC = _anim_dll.AddPrioritySqToAnimBlockC
_AddPrioritySqToAnimBlockC.restype = ctypes.c_bool
_AddPrioritySqToAnimBlockC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::AnimationBlock *
ctypes.c_void_p, # const CALUMI::UNIV::PriorityFrame *
ctypes.c_void_p, # unsigned int
ctypes.c_bool,
]

_GetPrioritySqArrayC = _anim_dll.GetPrioritySqArrayC
_GetPrioritySqArrayC.restype = ctypes.c_void_p # CALUMI::UNIV::PriorityFrame *

_GetPrioritySqArrayC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::AnimationBlock *
]

_GetPriorityFromSqC = _anim_dll.GetPriorityFromSqC
_GetPriorityFromSqC.restype = ctypes.c_void_p # CALUMI::UNIV::PriorityFrame *

_GetPriorityFromSqC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::AnimationBlock *
ctypes.c_int,
]

_GetPrioritySqSizeC = _anim_dll.GetPrioritySqSizeC
_GetPrioritySqSizeC.restype = ctypes.c_uint64
_GetPrioritySqSizeC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::AnimationBlock *
]

_CreateRotationFrameC = _anim_dll.CreateRotationFrameC
_CreateRotationFrameC.restype = ctypes.c_void_p # CALUMI::UNIV::RotationFrame *

_CreateRotationFrameC.argtypes = [
ctypes.c_uint16,
ctypes.c_float,
ctypes.c_float,
ctypes.c_float,
ctypes.c_float,
]

_CreateRotationFrameFromEulerC = _anim_dll.CreateRotationFrameFromEulerC
_CreateRotationFrameFromEulerC.restype = ctypes.c_void_p # CALUMI::UNIV::RotationFrame *

_CreateRotationFrameFromEulerC.argtypes = [
ctypes.c_uint16,
ctypes.c_float,
ctypes.c_float,
ctypes.c_float,
ctypes.c_uint8,
]

_DeleteRotationFrameC = _anim_dll.DeleteRotationFrameC
_DeleteRotationFrameC.restype = ctypes.c_int
_DeleteRotationFrameC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::RotationFrame **
]

_CreateTranslationFrameC = _anim_dll.CreateTranslationFrameC
_CreateTranslationFrameC.restype = ctypes.c_void_p # CALUMI::UNIV::TranslationFrame *

_CreateTranslationFrameC.argtypes = [
ctypes.c_uint16,
ctypes.c_double,
ctypes.c_double,
ctypes.c_double,
]

_DeleteTranslationFrameC = _anim_dll.DeleteTranslationFrameC
_DeleteTranslationFrameC.restype = ctypes.c_int
_DeleteTranslationFrameC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::TranslationFrame **
]

_CreateScalarFrameC = _anim_dll.CreateScalarFrameC
_CreateScalarFrameC.restype = ctypes.c_void_p # CALUMI::UNIV::ScalarFrame *

_CreateScalarFrameC.argtypes = [
ctypes.c_uint16,
ctypes.c_float,
]

_DeleteScalarFrameC = _anim_dll.DeleteScalarFrameC
_DeleteScalarFrameC.restype = ctypes.c_int
_DeleteScalarFrameC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::ScalarFrame **
]

_CreatePriorityFrameC = _anim_dll.CreatePriorityFrameC
_CreatePriorityFrameC.restype = ctypes.c_void_p # CALUMI::UNIV::PriorityFrame *

_CreatePriorityFrameC.argtypes = [
ctypes.c_uint16,
ctypes.c_uint8,
]

_DeletePriorityFrameC = _anim_dll.DeletePriorityFrameC
_DeletePriorityFrameC.restype = ctypes.c_int
_DeletePriorityFrameC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::PriorityFrame **
]

_GetFrameFromRotationFrameC = _anim_dll.GetFrameFromRotationFrameC
_GetFrameFromRotationFrameC.restype = ctypes.c_uint16
_GetFrameFromRotationFrameC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::RotationFrame *
]

_GetFrameFromTranslationFrameC = _anim_dll.GetFrameFromTranslationFrameC
_GetFrameFromTranslationFrameC.restype = ctypes.c_uint16
_GetFrameFromTranslationFrameC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::TranslationFrame *
]

_GetFrameFromScalarFrameC = _anim_dll.GetFrameFromScalarFrameC
_GetFrameFromScalarFrameC.restype = ctypes.c_uint16
_GetFrameFromScalarFrameC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::ScalarFrame *
]

_GetFrameFromPriorityFrameC = _anim_dll.GetFrameFromPriorityFrameC
_GetFrameFromPriorityFrameC.restype = ctypes.c_uint16
_GetFrameFromPriorityFrameC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::PriorityFrame *
]

_GetValueFromRotationFrameC = _anim_dll.GetValueFromRotationFrameC
_GetValueFromRotationFrameC.restype = ctypes.c_void_p # CALUMI::Math::Quaternion *

_GetValueFromRotationFrameC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::RotationFrame *
]

_GetValueFromTranslationFrameC = _anim_dll.GetValueFromTranslationFrameC
_GetValueFromTranslationFrameC.restype = ctypes.c_void_p # CALUMI::Math::Vector3D *

_GetValueFromTranslationFrameC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::TranslationFrame *
]

_GetValueFromScalarFrameC = _anim_dll.GetValueFromScalarFrameC
_GetValueFromScalarFrameC.restype = ctypes.c_float
_GetValueFromScalarFrameC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::ScalarFrame *
]

_GetValueFromPriorityFrameC = _anim_dll.GetValueFromPriorityFrameC
_GetValueFromPriorityFrameC.restype = ctypes.c_uint8
_GetValueFromPriorityFrameC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::PriorityFrame *
]

_CreateSkeletonRigC = _anim_dll.CreateSkeletonRigC
_CreateSkeletonRigC.restype = ctypes.c_void_p # CALUMI::UNIV::SkeletonRig *

_CreateSkeletonRigC.argtypes = [
ctypes.c_char_p,
]

_DeleteSkeletonRigC = _anim_dll.DeleteSkeletonRigC
_DeleteSkeletonRigC.restype = ctypes.c_int
_DeleteSkeletonRigC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::SkeletonRig **
]

_GetSkeletonRigRootC = _anim_dll.GetSkeletonRigRootC
_GetSkeletonRigRootC.restype = ctypes.c_void_p # CALUMI::UNIV::SkeletonBone *

_GetSkeletonRigRootC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::SkeletonRig *
]

_AddChildBoneC = _anim_dll.AddChildBoneC
_AddChildBoneC.restype = ctypes.c_void_p # CALUMI::UNIV::SkeletonBone *

_AddChildBoneC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::SkeletonBone *
ctypes.c_float,
ctypes.c_float,
ctypes.c_float,
ctypes.c_float,
ctypes.c_float,
ctypes.c_float,
ctypes.c_float,
ctypes.c_char_p,
]

_AddChildBoneWithEulerC = _anim_dll.AddChildBoneWithEulerC
_AddChildBoneWithEulerC.restype = ctypes.c_void_p # CALUMI::UNIV::SkeletonBone *

_AddChildBoneWithEulerC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::SkeletonBone *
ctypes.c_float,
ctypes.c_float,
ctypes.c_float,
ctypes.c_float,
ctypes.c_float,
ctypes.c_float,
ctypes.c_int,
ctypes.c_char_p,
]

_AddChildBoneWithVectorC = _anim_dll.AddChildBoneWithVectorC
_AddChildBoneWithVectorC.restype = ctypes.c_void_p # CALUMI::UNIV::SkeletonBone *

_AddChildBoneWithVectorC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::SkeletonBone *
ctypes.c_void_p, # const CALUMI::Math::Vector3 *
ctypes.c_void_p, # const CALUMI::Math::Quaternion *
ctypes.c_char_p,
]

_SetBoneTypeC = _anim_dll.SetBoneTypeC
_SetBoneTypeC.restype = ctypes.c_int
_SetBoneTypeC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::SkeletonBone *
ctypes.c_uint32,
]

_DeleteBoneC = _anim_dll.DeleteBoneC
_DeleteBoneC.restype = ctypes.c_int
_DeleteBoneC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::SkeletonBone **
]

_RenameBoneC = _anim_dll.RenameBoneC
_RenameBoneC.restype = ctypes.c_int
_RenameBoneC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::SkeletonRig *
ctypes.c_char_p,
ctypes.c_char_p,
]

_SetBoneTypeFromStringC = _anim_dll.SetBoneTypeFromStringC
_SetBoneTypeFromStringC.restype = ctypes.c_int
_SetBoneTypeFromStringC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::SkeletonBone *
ctypes.c_char_p,
]

_GetBoneTypeC = _anim_dll.GetBoneTypeC
_GetBoneTypeC.restype = ctypes.c_uint32
_GetBoneTypeC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::SkeletonBone *
]

_GetBoneTypeAsStringC = _anim_dll.GetBoneTypeAsStringC
_GetBoneTypeAsStringC.restype = ctypes.c_char_p
_GetBoneTypeAsStringC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::SkeletonBone *
]

_SetTwistBonePropertiesC = _anim_dll.SetTwistBonePropertiesC
_SetTwistBonePropertiesC.restype = ctypes.c_int
_SetTwistBonePropertiesC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::SkeletonBone *
ctypes.c_bool,
ctypes.c_char_p,
ctypes.c_float,
]

_GetTwistBoneDriverC = _anim_dll.GetTwistBoneDriverC
_GetTwistBoneDriverC.restype = ctypes.c_char_p
_GetTwistBoneDriverC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::SkeletonBone *
]

_GetTwistBoneDriverWeightC = _anim_dll.GetTwistBoneDriverWeightC
_GetTwistBoneDriverWeightC.restype = ctypes.c_float
_GetTwistBoneDriverWeightC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::SkeletonBone *
]

_GetSkeletonRigBoneCountC = _anim_dll.GetSkeletonRigBoneCountC
_GetSkeletonRigBoneCountC.restype = ctypes.c_uint # unsigned int

_GetSkeletonRigBoneCountC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::SkeletonRig *
]

_GetSkeletonRigAnimatedBoneCountC = _anim_dll.GetSkeletonRigAnimatedBoneCountC
_GetSkeletonRigAnimatedBoneCountC.restype = ctypes.c_uint

_GetSkeletonRigAnimatedBoneCountC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::SkeletonRig *
]

_GetSkeletonRigNonAnimatedBoneCountC = _anim_dll.GetSkeletonRigNonAnimatedBoneCountC
_GetSkeletonRigNonAnimatedBoneCountC.restype = ctypes.c_uint

_GetSkeletonRigNonAnimatedBoneCountC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::SkeletonRig *
]

_GetSkeletonRigBoneTypeCountC = _anim_dll.GetSkeletonRigBoneTypeCountC
_GetSkeletonRigBoneTypeCountC.restype = ctypes.c_uint

_GetSkeletonRigBoneTypeCountC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::SkeletonRig *
ctypes.c_uint32,
]

_GetSkeletonRigNameC = _anim_dll.GetSkeletonRigNameC
_GetSkeletonRigNameC.restype = ctypes.c_char_p
_GetSkeletonRigNameC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::SkeletonRig *
]

_GetSkeletonBoneC = _anim_dll.GetSkeletonBoneC
_GetSkeletonBoneC.restype = ctypes.c_void_p # const CALUMI::UNIV::SkeletonBone *

_GetSkeletonBoneC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::SkeletonRig *
ctypes.c_char_p,
]

_GetSkeletonBoneNameC = _anim_dll.GetSkeletonBoneNameC
_GetSkeletonBoneNameC.restype = ctypes.c_char_p
_GetSkeletonBoneNameC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::SkeletonBone *
]

_GetSkeletonBoneParentC = _anim_dll.GetSkeletonBoneParentC
_GetSkeletonBoneParentC.restype = ctypes.c_void_p # const CALUMI::UNIV::SkeletonBone *

_GetSkeletonBoneParentC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::SkeletonBone *
]

_GetSkeletonBoneChildC = _anim_dll.GetSkeletonBoneChildC
_GetSkeletonBoneChildC.restype = ctypes.c_void_p # const CALUMI::UNIV::SkeletonBone *

_GetSkeletonBoneChildC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::SkeletonBone *
ctypes.c_uint, # unsigned int
]

_GetSkeletonBoneChildWithNameC = _anim_dll.GetSkeletonBoneChildWithNameC
_GetSkeletonBoneChildWithNameC.restype = ctypes.c_void_p # const CALUMI::UNIV::SkeletonBone *

_GetSkeletonBoneChildWithNameC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::SkeletonBone *
ctypes.c_char_p,
ctypes.c_bool,
]

_GetGlobalSkeletonBoneRotationC = _anim_dll.GetGlobalSkeletonBoneRotationC
_GetGlobalSkeletonBoneRotationC.restype = ctypes.c_void_p # const CALUMI::Math::Quaternion *

_GetGlobalSkeletonBoneRotationC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::SkeletonBone *
]

_GetLocalSkeletonBoneRotationC = _anim_dll.GetLocalSkeletonBoneRotationC
_GetLocalSkeletonBoneRotationC.restype = ctypes.c_void_p # const CALUMI::Math::Quaternion *

_GetLocalSkeletonBoneRotationC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::SkeletonBone *
]

_GetGlobalSkeletonBonePositionC = _anim_dll.GetGlobalSkeletonBonePositionC
_GetGlobalSkeletonBonePositionC.restype = ctypes.c_void_p # const CALUMI::Math::Vector3 *

_GetGlobalSkeletonBonePositionC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::SkeletonBone *
]

_GetLocalSkeletonBonePositionC = _anim_dll.GetLocalSkeletonBonePositionC
_GetLocalSkeletonBonePositionC.restype = ctypes.c_void_p # const CALUMI::Math::Vector3 *

_GetLocalSkeletonBonePositionC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::SkeletonBone *
]

_SetGlobalSkeletonBonePositionC = _anim_dll.SetGlobalSkeletonBonePositionC
_SetGlobalSkeletonBonePositionC.restype = ctypes.c_int
_SetGlobalSkeletonBonePositionC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::SkeletonBone *
ctypes.c_float,
ctypes.c_float,
ctypes.c_float,
]

_SetLocalSkeletonBonePositionC = _anim_dll.SetLocalSkeletonBonePositionC
_SetLocalSkeletonBonePositionC.restype = ctypes.c_int
_SetLocalSkeletonBonePositionC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::SkeletonBone *
ctypes.c_float,
ctypes.c_float,
ctypes.c_float,
]

_SetGlobalSkeletonBoneRotationC = _anim_dll.SetGlobalSkeletonBoneRotationC
_SetGlobalSkeletonBoneRotationC.restype = ctypes.c_int
_SetGlobalSkeletonBoneRotationC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::SkeletonBone *
ctypes.c_float,
ctypes.c_float,
ctypes.c_float,
ctypes.c_float,
]

_SetLocalSkeletonBoneRotationC = _anim_dll.SetLocalSkeletonBoneRotationC
_SetLocalSkeletonBoneRotationC.restype = ctypes.c_int
_SetLocalSkeletonBoneRotationC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::SkeletonBone *
ctypes.c_float,
ctypes.c_float,
ctypes.c_float,
ctypes.c_float,
]

_SetGlobalSkeletonBoneRotationWithEulerC = _anim_dll.SetGlobalSkeletonBoneRotationWithEulerC
_SetGlobalSkeletonBoneRotationWithEulerC.restype = ctypes.c_int
_SetGlobalSkeletonBoneRotationWithEulerC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::SkeletonBone *
ctypes.c_float,
ctypes.c_float,
ctypes.c_float,
ctypes.c_int,
]

_SetLocalSkeletonBoneRotationWithEulerC = _anim_dll.SetLocalSkeletonBoneRotationWithEulerC
_SetLocalSkeletonBoneRotationWithEulerC.restype = ctypes.c_int
_SetLocalSkeletonBoneRotationWithEulerC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::SkeletonBone *
ctypes.c_float,
ctypes.c_float,
ctypes.c_float,
ctypes.c_int,
]

_SetGlobalSkeletonBoneTransformC = _anim_dll.SetGlobalSkeletonBoneTransformC
_SetGlobalSkeletonBoneTransformC.restype = ctypes.c_int
_SetGlobalSkeletonBoneTransformC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::SkeletonBone *
ctypes.c_float,
ctypes.c_float,
ctypes.c_float,
ctypes.c_float,
ctypes.c_float,
ctypes.c_float,
ctypes.c_float,
]

_SetLocalSkeletonBoneTransformC = _anim_dll.SetLocalSkeletonBoneTransformC
_SetLocalSkeletonBoneTransformC.restype = ctypes.c_int
_SetLocalSkeletonBoneTransformC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::SkeletonBone *
ctypes.c_float,
ctypes.c_float,
ctypes.c_float,
ctypes.c_float,
ctypes.c_float,
ctypes.c_float,
ctypes.c_float,
]

_SetGlobalSkeletonBoneTransformWithEulerC = _anim_dll.SetGlobalSkeletonBoneTransformWithEulerC
_SetGlobalSkeletonBoneTransformWithEulerC.restype = ctypes.c_int
_SetGlobalSkeletonBoneTransformWithEulerC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::SkeletonBone *
ctypes.c_float,
ctypes.c_float,
ctypes.c_float,
ctypes.c_float,
ctypes.c_float,
ctypes.c_float,
ctypes.c_int,
]

_SetLocalSkeletonBoneTransformWithEulerC = _anim_dll.SetLocalSkeletonBoneTransformWithEulerC
_SetLocalSkeletonBoneTransformWithEulerC.restype = ctypes.c_int
_SetLocalSkeletonBoneTransformWithEulerC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::SkeletonBone *
ctypes.c_float,
ctypes.c_float,
ctypes.c_float,
ctypes.c_float,
ctypes.c_float,
ctypes.c_float,
ctypes.c_int,
]

_SetSkeletonBoneParentC = _anim_dll.SetSkeletonBoneParentC
_SetSkeletonBoneParentC.restype = ctypes.c_int
_SetSkeletonBoneParentC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::SkeletonBone *
ctypes.c_void_p, # const CALUMI::UNIV::SkeletonBone *
]

_CreateStringContainerC = _anim_dll.CreateStringContainerC
_CreateStringContainerC.restype = ctypes.c_void_p # CALUMI::Utilities::StringContainer *

_CreateStringContainerC.argtypes = [

]

_GetStringFromContainerC = _anim_dll.GetStringFromContainerC
_GetStringFromContainerC.restype = ctypes.c_char_p
_GetStringFromContainerC.argtypes = [
ctypes.c_void_p, # const CALUMI::Utilities::StringContainer *
]

_GetStringContainerSizeC = _anim_dll.GetStringContainerSizeC
_GetStringContainerSizeC.restype = ctypes.c_uint64
_GetStringContainerSizeC.argtypes = [
ctypes.c_void_p, # const CALUMI::Utilities::StringContainer *
]

_DeleteStringContainerC = _anim_dll.DeleteStringContainerC
_DeleteStringContainerC.restype = ctypes.c_void_p # void

_DeleteStringContainerC.argtypes = [
ctypes.c_void_p, # const CALUMI::Utilities::StringContainer **
]

