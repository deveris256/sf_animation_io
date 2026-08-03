import ctypes
import os
import sys

if sys.platform == "win32":
    dll_name = "CALUMI.Animation.dll"
elif sys.platform == "linux":
    dll_name = "libCALUMI.Animation.so"
else:
    raise Exception("ANIMATION IO: CANNOT DETERMINE PLATFORM")

_anim_dll = ctypes.CDLL(os.path.join(os.path.dirname(os.path.dirname(__file__)),dll_name))
PATH_FOR_IMPORT_JSON = "C:\\General Files\\Git\\AnimScript\\AnimStarfieldMeshConverter_repo\\scripts\\tool_export_mesh\\ExportedJSONs\\LastFile.json"

def _list_to_wchar_arr(python_list):
    arr = (ctypes.c_wchar_p * len(python_list))()
    arr[:] = python_list
    return arr

_CreateVector2C = _anim_dll.CreateVector2C
_CreateVector2C.restype = ctypes.c_void_p # CALUMI::Math::Vector2 *

_CreateVector2C.argtypes = [
ctypes.c_float,
ctypes.c_float,
]

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
ctypes.c_void_p, # const CALUMI::Math::Vector2 **
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
ctypes.c_void_p, # const CALUMI::Math::Vector2D **
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
ctypes.c_void_p, # const CALUMI::Math::Vector3 **
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
ctypes.c_void_p, # const CALUMI::Math::Vector3D **
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
ctypes.c_void_p, # const CALUMI::Math::Transform **
]

_CreateQuaternionC = _anim_dll.CreateQuaternionC
_CreateQuaternionC.restype = ctypes.c_void_p # CALUMI::Math::Quaternion *

_CreateQuaternionC.argtypes = [
ctypes.c_float,
ctypes.c_float,
ctypes.c_float,
ctypes.c_float,
]

_CreateQuaternionFromEulerC = _anim_dll.CreateQuaternionFromEulerC
_CreateQuaternionFromEulerC.restype = ctypes.c_void_p # CALUMI::Math::Quaternion *

_CreateQuaternionFromEulerC.argtypes = [
ctypes.c_float,
ctypes.c_float,
ctypes.c_float,
ctypes.c_int,
]

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
ctypes.c_void_p, # const CALUMI::Math::Quaternion **
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
ctypes.c_void_p, # const wchar_t *
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

_SFBGSAnimationPackage_AddPackageToAnimationC = _anim_dll.SFBGSAnimationPackage_AddPackageToAnimationC
_SFBGSAnimationPackage_AddPackageToAnimationC.restype = ctypes.c_int
_SFBGSAnimationPackage_AddPackageToAnimationC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::Animation *
ctypes.c_bool,
]

_SFBGSAnimationPackage_RemovePackageFromAnimationC = _anim_dll.SFBGSAnimationPackage_RemovePackageFromAnimationC
_SFBGSAnimationPackage_RemovePackageFromAnimationC.restype = ctypes.c_int
_SFBGSAnimationPackage_RemovePackageFromAnimationC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::Animation *
]

_SFBGSAnimationPackage_HasAmendedBlockC = _anim_dll.SFBGSAnimationPackage_HasAmendedBlockC
_SFBGSAnimationPackage_HasAmendedBlockC.restype = ctypes.c_int
_SFBGSAnimationPackage_HasAmendedBlockC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::Animation *
ctypes.c_char_p,
]

_SFBGSAnimationPackage_HasAmendedBlockHashC = _anim_dll.SFBGSAnimationPackage_HasAmendedBlockHashC
_SFBGSAnimationPackage_HasAmendedBlockHashC.restype = ctypes.c_int
_SFBGSAnimationPackage_HasAmendedBlockHashC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::Animation *
ctypes.c_uint32,
]

_SFBGSAnimationPackage_GetAmendedBlockCountC = _anim_dll.SFBGSAnimationPackage_GetAmendedBlockCountC
_SFBGSAnimationPackage_GetAmendedBlockCountC.restype = ctypes.c_int
_SFBGSAnimationPackage_GetAmendedBlockCountC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::Animation *
]

_SFBGSAnimationPackage_OverrideRigWithDefaultPrecisionC = _anim_dll.SFBGSAnimationPackage_OverrideRigWithDefaultPrecisionC
_SFBGSAnimationPackage_OverrideRigWithDefaultPrecisionC.restype = ctypes.c_int
_SFBGSAnimationPackage_OverrideRigWithDefaultPrecisionC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::Animation *
]

_SFBGSAnimationPackage_OverrideRigWith1stPersonPrecisionC = _anim_dll.SFBGSAnimationPackage_OverrideRigWith1stPersonPrecisionC
_SFBGSAnimationPackage_OverrideRigWith1stPersonPrecisionC.restype = ctypes.c_int
_SFBGSAnimationPackage_OverrideRigWith1stPersonPrecisionC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::Animation *
]

_SFBGSAnimationPackage_OverrideRigWithShipPrecisionC = _anim_dll.SFBGSAnimationPackage_OverrideRigWithShipPrecisionC
_SFBGSAnimationPackage_OverrideRigWithShipPrecisionC.restype = ctypes.c_int
_SFBGSAnimationPackage_OverrideRigWithShipPrecisionC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::Animation *
]

_SFBGSAnimationPackage_OverrideRigWithCustomPrecisionC = _anim_dll.SFBGSAnimationPackage_OverrideRigWithCustomPrecisionC
_SFBGSAnimationPackage_OverrideRigWithCustomPrecisionC.restype = ctypes.c_int
_SFBGSAnimationPackage_OverrideRigWithCustomPrecisionC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::Animation *
ctypes.c_float,
ctypes.c_float,
]

_SFBGSAnimationPackage_GetOverridePrecisionHighC = _anim_dll.SFBGSAnimationPackage_GetOverridePrecisionHighC
_SFBGSAnimationPackage_GetOverridePrecisionHighC.restype = ctypes.c_float
_SFBGSAnimationPackage_GetOverridePrecisionHighC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::Animation *
]

_SFBGSAnimationPackage_GetOverridePrecisionLowC = _anim_dll.SFBGSAnimationPackage_GetOverridePrecisionLowC
_SFBGSAnimationPackage_GetOverridePrecisionLowC.restype = ctypes.c_float
_SFBGSAnimationPackage_GetOverridePrecisionLowC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::Animation *
]

_SFBGSAnimationPackage_GetPrecisionSet = _anim_dll.SFBGSAnimationPackage_GetPrecisionSet
_SFBGSAnimationPackage_GetPrecisionSet.restype = ctypes.c_char_p
_SFBGSAnimationPackage_GetPrecisionSet.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::Animation *
]

_SFBGSAnimationPackage_UsesRigPrecision = _anim_dll.SFBGSAnimationPackage_UsesRigPrecision
_SFBGSAnimationPackage_UsesRigPrecision.restype = ctypes.c_int
_SFBGSAnimationPackage_UsesRigPrecision.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::Animation *
]

_SFBGSAnimationPackage_ResetPrecision = _anim_dll.SFBGSAnimationPackage_ResetPrecision
_SFBGSAnimationPackage_ResetPrecision.restype = ctypes.c_int
_SFBGSAnimationPackage_ResetPrecision.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::Animation *
]

_SFBGSAnimationPackage_AddAmendedBlockWithNameC = _anim_dll.SFBGSAnimationPackage_AddAmendedBlockWithNameC
_SFBGSAnimationPackage_AddAmendedBlockWithNameC.restype = ctypes.c_int
_SFBGSAnimationPackage_AddAmendedBlockWithNameC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::Animation *
ctypes.c_void_p, # const CALUMI::UNIV::AnimationBlock *
ctypes.c_bool,
]

_SFBGSAnimationPackage_AddAmendedBlockWithHashC = _anim_dll.SFBGSAnimationPackage_AddAmendedBlockWithHashC
_SFBGSAnimationPackage_AddAmendedBlockWithHashC.restype = ctypes.c_int
_SFBGSAnimationPackage_AddAmendedBlockWithHashC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::Animation *
ctypes.c_uint32,
ctypes.c_void_p, # const CALUMI::UNIV::AnimationBlock *
ctypes.c_bool,
]

_SFBGSAnimationPackage_RemoveAmendedBlockWithNameC = _anim_dll.SFBGSAnimationPackage_RemoveAmendedBlockWithNameC
_SFBGSAnimationPackage_RemoveAmendedBlockWithNameC.restype = ctypes.c_int
_SFBGSAnimationPackage_RemoveAmendedBlockWithNameC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::Animation *
ctypes.c_char_p,
]

_SFBGSAnimationPackage_RemoveAmendedBlockWithHashC = _anim_dll.SFBGSAnimationPackage_RemoveAmendedBlockWithHashC
_SFBGSAnimationPackage_RemoveAmendedBlockWithHashC.restype = ctypes.c_int
_SFBGSAnimationPackage_RemoveAmendedBlockWithHashC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::Animation *
ctypes.c_uint32,
]

_SFBGSAnimationPackage_RemoveAmendedBlockWithIndexC = _anim_dll.SFBGSAnimationPackage_RemoveAmendedBlockWithIndexC
_SFBGSAnimationPackage_RemoveAmendedBlockWithIndexC.restype = ctypes.c_int
_SFBGSAnimationPackage_RemoveAmendedBlockWithIndexC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::Animation *
ctypes.c_uint16,
]

_SFBGSAnimationPackage_HasAmendedBlockWithNameC = _anim_dll.SFBGSAnimationPackage_HasAmendedBlockWithNameC
_SFBGSAnimationPackage_HasAmendedBlockWithNameC.restype = ctypes.c_int
_SFBGSAnimationPackage_HasAmendedBlockWithNameC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::Animation *
ctypes.c_char_p,
]

_SFBGSAnimationPackage_HasAmendedBlockWithHashC = _anim_dll.SFBGSAnimationPackage_HasAmendedBlockWithHashC
_SFBGSAnimationPackage_HasAmendedBlockWithHashC.restype = ctypes.c_int
_SFBGSAnimationPackage_HasAmendedBlockWithHashC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::Animation *
ctypes.c_uint32,
]

_SFBGSAnimationPackage_FindAmendedBlockWithNameC = _anim_dll.SFBGSAnimationPackage_FindAmendedBlockWithNameC
_SFBGSAnimationPackage_FindAmendedBlockWithNameC.restype = ctypes.c_int
_SFBGSAnimationPackage_FindAmendedBlockWithNameC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::Animation *
ctypes.c_char_p,
]

_SFBGSAnimationPackage_FindAmendedBlockWithHashC = _anim_dll.SFBGSAnimationPackage_FindAmendedBlockWithHashC
_SFBGSAnimationPackage_FindAmendedBlockWithHashC.restype = ctypes.c_int
_SFBGSAnimationPackage_FindAmendedBlockWithHashC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::Animation *
ctypes.c_uint32,
]

_SFBGSRigPackage_AddPackageToSkeletonRigC = _anim_dll.SFBGSRigPackage_AddPackageToSkeletonRigC
_SFBGSRigPackage_AddPackageToSkeletonRigC.restype = ctypes.c_int
_SFBGSRigPackage_AddPackageToSkeletonRigC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::SkeletonRig *
ctypes.c_bool,
]

_SFBGSRigPackage_RemoveRigPackageFromSkeletonRigC = _anim_dll.SFBGSRigPackage_RemoveRigPackageFromSkeletonRigC
_SFBGSRigPackage_RemoveRigPackageFromSkeletonRigC.restype = ctypes.c_int
_SFBGSRigPackage_RemoveRigPackageFromSkeletonRigC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::SkeletonRig *
]

_SFBGSRigPackage_BoneIsMappedC = _anim_dll.SFBGSRigPackage_BoneIsMappedC
_SFBGSRigPackage_BoneIsMappedC.restype = ctypes.c_int
_SFBGSRigPackage_BoneIsMappedC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::SkeletonRig *
ctypes.c_char_p,
]

_SFBGSRigPackage_KeyIsMappedC = _anim_dll.SFBGSRigPackage_KeyIsMappedC
_SFBGSRigPackage_KeyIsMappedC.restype = ctypes.c_int
_SFBGSRigPackage_KeyIsMappedC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::SkeletonRig *
ctypes.c_uint8,
]

_SFBGSRigPackage_AddBoneNameToMapC = _anim_dll.SFBGSRigPackage_AddBoneNameToMapC
_SFBGSRigPackage_AddBoneNameToMapC.restype = ctypes.c_int
_SFBGSRigPackage_AddBoneNameToMapC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::SkeletonRig *
ctypes.c_uint8,
ctypes.c_char_p,
ctypes.c_bool,
]

_SFBGSRigPackage_AddBoneToMapC = _anim_dll.SFBGSRigPackage_AddBoneToMapC
_SFBGSRigPackage_AddBoneToMapC.restype = ctypes.c_int
_SFBGSRigPackage_AddBoneToMapC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::SkeletonRig *
ctypes.c_uint8,
ctypes.c_void_p, # const CALUMI::UNIV::SkeletonBone *
ctypes.c_bool,
]

_SFBGSRigPackage_RemoveBoneFromMapUsingKeyC = _anim_dll.SFBGSRigPackage_RemoveBoneFromMapUsingKeyC
_SFBGSRigPackage_RemoveBoneFromMapUsingKeyC.restype = ctypes.c_int
_SFBGSRigPackage_RemoveBoneFromMapUsingKeyC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::SkeletonRig *
ctypes.c_uint8,
]

_SFBGSRigPackage_RemoveBoneFromMapUsingNameC = _anim_dll.SFBGSRigPackage_RemoveBoneFromMapUsingNameC
_SFBGSRigPackage_RemoveBoneFromMapUsingNameC.restype = ctypes.c_int
_SFBGSRigPackage_RemoveBoneFromMapUsingNameC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::SkeletonRig *
ctypes.c_char_p,
]

_SFBGSRigPackage_GetBoneKeyC = _anim_dll.SFBGSRigPackage_GetBoneKeyC
_SFBGSRigPackage_GetBoneKeyC.restype = ctypes.c_uint8
_SFBGSRigPackage_GetBoneKeyC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::SkeletonRig *
ctypes.c_char_p,
]

_SFBGSRigPackage_GetBoneNameFromKeyC = _anim_dll.SFBGSRigPackage_GetBoneNameFromKeyC
_SFBGSRigPackage_GetBoneNameFromKeyC.restype = ctypes.c_char_p
_SFBGSRigPackage_GetBoneNameFromKeyC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::SkeletonRig *
ctypes.c_uint8,
]

_SFBGSRigPackage_SetMannequinC = _anim_dll.SFBGSRigPackage_SetMannequinC
_SFBGSRigPackage_SetMannequinC.restype = ctypes.c_int
_SFBGSRigPackage_SetMannequinC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::SkeletonRig *
ctypes.c_bool,
]

_SFBGSRigPackage_IsMannequinC = _anim_dll.SFBGSRigPackage_IsMannequinC
_SFBGSRigPackage_IsMannequinC.restype = ctypes.c_int
_SFBGSRigPackage_IsMannequinC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::SkeletonRig *
]

_SFBGSRigPackage_GetRigMapSize = _anim_dll.SFBGSRigPackage_GetRigMapSize
_SFBGSRigPackage_GetRigMapSize.restype = ctypes.c_uint64
_SFBGSRigPackage_GetRigMapSize.argtypes = [

]

_SFBGSRigPackage_SetPrecisionToDefaultC = _anim_dll.SFBGSRigPackage_SetPrecisionToDefaultC
_SFBGSRigPackage_SetPrecisionToDefaultC.restype = ctypes.c_int
_SFBGSRigPackage_SetPrecisionToDefaultC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::SkeletonRig *
]

_SFBGSRigPackage_SetPrecisionToFirstPersonC = _anim_dll.SFBGSRigPackage_SetPrecisionToFirstPersonC
_SFBGSRigPackage_SetPrecisionToFirstPersonC.restype = ctypes.c_int
_SFBGSRigPackage_SetPrecisionToFirstPersonC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::SkeletonRig *
]

_SFBGSRigPackage_SetPrecisionToShipValuesC = _anim_dll.SFBGSRigPackage_SetPrecisionToShipValuesC
_SFBGSRigPackage_SetPrecisionToShipValuesC.restype = ctypes.c_int
_SFBGSRigPackage_SetPrecisionToShipValuesC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::SkeletonRig *
]

_SFBGSRigPackage_SetPrecisionToCustomC = _anim_dll.SFBGSRigPackage_SetPrecisionToCustomC
_SFBGSRigPackage_SetPrecisionToCustomC.restype = ctypes.c_int
_SFBGSRigPackage_SetPrecisionToCustomC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::SkeletonRig *
ctypes.c_float,
ctypes.c_float,
]

_SFBGSRigPackage_GetPrecisionType = _anim_dll.SFBGSRigPackage_GetPrecisionType
_SFBGSRigPackage_GetPrecisionType.restype = ctypes.c_char_p
_SFBGSRigPackage_GetPrecisionType.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::SkeletonRig *
]

_SFBGSRigPackage_GetHighPrecisionValueC = _anim_dll.SFBGSRigPackage_GetHighPrecisionValueC
_SFBGSRigPackage_GetHighPrecisionValueC.restype = ctypes.c_float
_SFBGSRigPackage_GetHighPrecisionValueC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::SkeletonRig *
]

_SFBGSRigPackage_GetLowPrecisionValueC = _anim_dll.SFBGSRigPackage_GetLowPrecisionValueC
_SFBGSRigPackage_GetLowPrecisionValueC.restype = ctypes.c_float
_SFBGSRigPackage_GetLowPrecisionValueC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::SkeletonRig *
]

_SFBGSRigPackage_GetBoneLODValueC = _anim_dll.SFBGSRigPackage_GetBoneLODValueC
_SFBGSRigPackage_GetBoneLODValueC.restype = ctypes.c_int
_SFBGSRigPackage_GetBoneLODValueC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::SkeletonRig *
ctypes.c_char_p,
]

_SFBGSRigPackage_SetBoneLODValueC = _anim_dll.SFBGSRigPackage_SetBoneLODValueC
_SFBGSRigPackage_SetBoneLODValueC.restype = ctypes.c_int
_SFBGSRigPackage_SetBoneLODValueC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::SkeletonRig *
ctypes.c_char_p,
ctypes.c_int,
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
_GetLastFrameInAnimBlockC.restype = ctypes.c_void_p # unsigned int

_GetLastFrameInAnimBlockC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::AnimationBlock *
]

_AddRotationSqToAnimBlockC = _anim_dll.AddRotationSqToAnimBlockC
_AddRotationSqToAnimBlockC.restype = ctypes.c_void_p # unsigned int

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

_ExecuteRDPReduction_RotationC = _anim_dll.ExecuteRDPReduction_RotationC
_ExecuteRDPReduction_RotationC.restype = ctypes.c_int
_ExecuteRDPReduction_RotationC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::AnimationBlock *
ctypes.c_float,
]

_AddTranslationSqToAnimBlockC = _anim_dll.AddTranslationSqToAnimBlockC
_AddTranslationSqToAnimBlockC.restype = ctypes.c_void_p # unsigned int

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

_ExecuteRDPReduction_TranslationC = _anim_dll.ExecuteRDPReduction_TranslationC
_ExecuteRDPReduction_TranslationC.restype = ctypes.c_int
_ExecuteRDPReduction_TranslationC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::AnimationBlock *
ctypes.c_float,
]

_AddScalarSqToAnimBlockC = _anim_dll.AddScalarSqToAnimBlockC
_AddScalarSqToAnimBlockC.restype = ctypes.c_void_p # unsigned int

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

_ExecuteRDPReduction_ScalarC = _anim_dll.ExecuteRDPReduction_ScalarC
_ExecuteRDPReduction_ScalarC.restype = ctypes.c_int
_ExecuteRDPReduction_ScalarC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::AnimationBlock *
ctypes.c_float,
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
ctypes.c_void_p, # CALUMI::UNIV::SkeletonRig **
]

_GetSkeletonRigRootC = _anim_dll.GetSkeletonRigRootC
_GetSkeletonRigRootC.restype = ctypes.c_void_p # const CALUMI::UNIV::SkeletonBone *

_GetSkeletonRigRootC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::SkeletonRig *
]

_GetSkeletonRigRootFromBoneC = _anim_dll.GetSkeletonRigRootFromBoneC
_GetSkeletonRigRootFromBoneC.restype = ctypes.c_void_p # const CALUMI::UNIV::SkeletonBone *

_GetSkeletonRigRootFromBoneC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::SkeletonBone *
]

_GetSkeletonRigFromBoneC = _anim_dll.GetSkeletonRigFromBoneC
_GetSkeletonRigFromBoneC.restype = ctypes.c_void_p # const CALUMI::UNIV::SkeletonRig *

_GetSkeletonRigFromBoneC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::SkeletonBone *
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
_GetSkeletonRigBoneCountC.restype = ctypes.c_void_p # unsigned int

_GetSkeletonRigBoneCountC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::SkeletonRig *
]

_GetSkeletonRigAnimatedBoneCountC = _anim_dll.GetSkeletonRigAnimatedBoneCountC
_GetSkeletonRigAnimatedBoneCountC.restype = ctypes.c_void_p # unsigned int

_GetSkeletonRigAnimatedBoneCountC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::SkeletonRig *
]

_GetSkeletonRigNonAnimatedBoneCountC = _anim_dll.GetSkeletonRigNonAnimatedBoneCountC
_GetSkeletonRigNonAnimatedBoneCountC.restype = ctypes.c_void_p # unsigned int

_GetSkeletonRigNonAnimatedBoneCountC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::SkeletonRig *
]

_GetSkeletonRigBoneTypeCountC = _anim_dll.GetSkeletonRigBoneTypeCountC
_GetSkeletonRigBoneTypeCountC.restype = ctypes.c_void_p # unsigned int

_GetSkeletonRigBoneTypeCountC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::SkeletonRig *
ctypes.c_uint32,
]

_GetSkeletonBoneChildCountC = _anim_dll.GetSkeletonBoneChildCountC
_GetSkeletonBoneChildCountC.restype = ctypes.c_void_p # unsigned int

_GetSkeletonBoneChildCountC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::SkeletonBone *
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
ctypes.c_void_p, # unsigned int
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

_GetLocalSkeletonBoneTransformC = _anim_dll.GetLocalSkeletonBoneTransformC
_GetLocalSkeletonBoneTransformC.restype = ctypes.c_void_p # const CALUMI::Math::Transform *

_GetLocalSkeletonBoneTransformC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::SkeletonBone *
]

_GetGlobalSkeletonBoneTransformC = _anim_dll.GetGlobalSkeletonBoneTransformC
_GetGlobalSkeletonBoneTransformC.restype = ctypes.c_void_p # const CALUMI::Math::Transform *

_GetGlobalSkeletonBoneTransformC.argtypes = [
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

_UNIVManifestRigPackage_AddPackageToSkeletonRigC = _anim_dll.UNIVManifestRigPackage_AddPackageToSkeletonRigC
_UNIVManifestRigPackage_AddPackageToSkeletonRigC.restype = ctypes.c_int
_UNIVManifestRigPackage_AddPackageToSkeletonRigC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::SkeletonRig *
ctypes.c_bool,
]

_UNIVManifestRigPackage_RemoveRigPackageFromSkeletonRigC = _anim_dll.UNIVManifestRigPackage_RemoveRigPackageFromSkeletonRigC
_UNIVManifestRigPackage_RemoveRigPackageFromSkeletonRigC.restype = ctypes.c_int
_UNIVManifestRigPackage_RemoveRigPackageFromSkeletonRigC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::SkeletonRig *
]

_UNIVManifestRigPackage_AddBoneC = _anim_dll.UNIVManifestRigPackage_AddBoneC
_UNIVManifestRigPackage_AddBoneC.restype = ctypes.c_int
_UNIVManifestRigPackage_AddBoneC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::SkeletonRig *
ctypes.c_char_p,
]

_UNIVManifestRigPackage_InsertBoneC = _anim_dll.UNIVManifestRigPackage_InsertBoneC
_UNIVManifestRigPackage_InsertBoneC.restype = ctypes.c_int
_UNIVManifestRigPackage_InsertBoneC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::SkeletonRig *
ctypes.c_char_p,
ctypes.c_uint, # unsigned int
]

_UNIVManifestRigPackage_RemoveBoneC = _anim_dll.UNIVManifestRigPackage_RemoveBoneC
_UNIVManifestRigPackage_RemoveBoneC.restype = ctypes.c_int
_UNIVManifestRigPackage_RemoveBoneC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::SkeletonRig *
ctypes.c_char_p,
]

_UNIVManifestRigPackage_GetCountC = _anim_dll.UNIVManifestRigPackage_GetCountC
_UNIVManifestRigPackage_GetCountC.restype = ctypes.c_void_p # int64_t

_UNIVManifestRigPackage_GetCountC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::SkeletonRig *
]

_UNIVManifestRigPackage_GetBoneC = _anim_dll.UNIVManifestRigPackage_GetBoneC
_UNIVManifestRigPackage_GetBoneC.restype = ctypes.c_char_p
_UNIVManifestRigPackage_GetBoneC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::SkeletonRig *
ctypes.c_void_p, # unsigned int
]

_UNIVMirrorRigPackage_AddPackageToSkeletonRigC = _anim_dll.UNIVMirrorRigPackage_AddPackageToSkeletonRigC
_UNIVMirrorRigPackage_AddPackageToSkeletonRigC.restype = ctypes.c_int
_UNIVMirrorRigPackage_AddPackageToSkeletonRigC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::SkeletonRig *
ctypes.c_bool,
]

_UNIVMirrorRigPackage_RemoveRigPackageFromSkeletonRigC = _anim_dll.UNIVMirrorRigPackage_RemoveRigPackageFromSkeletonRigC
_UNIVMirrorRigPackage_RemoveRigPackageFromSkeletonRigC.restype = ctypes.c_int
_UNIVMirrorRigPackage_RemoveRigPackageFromSkeletonRigC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::SkeletonRig *
]

_UNIVMirrorRigPackage_AddPairToRigPackageFromSkeletonRigC = _anim_dll.UNIVMirrorRigPackage_AddPairToRigPackageFromSkeletonRigC
_UNIVMirrorRigPackage_AddPairToRigPackageFromSkeletonRigC.restype = ctypes.c_int
_UNIVMirrorRigPackage_AddPairToRigPackageFromSkeletonRigC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::SkeletonRig *
ctypes.c_char_p,
ctypes.c_char_p,
]

_UNIVMirrorRigPackage_GetPairCountC = _anim_dll.UNIVMirrorRigPackage_GetPairCountC
_UNIVMirrorRigPackage_GetPairCountC.restype = ctypes.c_void_p # int64_t

_UNIVMirrorRigPackage_GetPairCountC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::SkeletonRig *
]

_UNIVMirrorRigPackage_GetFirstOfPairEntryC = _anim_dll.UNIVMirrorRigPackage_GetFirstOfPairEntryC
_UNIVMirrorRigPackage_GetFirstOfPairEntryC.restype = ctypes.c_char_p
_UNIVMirrorRigPackage_GetFirstOfPairEntryC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::SkeletonRig *
ctypes.c_void_p, # unsigned int
]

_UNIVMirrorRigPackage_GetSecondOfPairEntryC = _anim_dll.UNIVMirrorRigPackage_GetSecondOfPairEntryC
_UNIVMirrorRigPackage_GetSecondOfPairEntryC.restype = ctypes.c_char_p
_UNIVMirrorRigPackage_GetSecondOfPairEntryC.argtypes = [
ctypes.c_void_p, # const CALUMI::UNIV::SkeletonRig *
ctypes.c_void_p, # unsigned int
]

_BGS_Str_CRC32C = _anim_dll.BGS_Str_CRC32C
_BGS_Str_CRC32C.restype = ctypes.c_uint32
_BGS_Str_CRC32C.argtypes = [
ctypes.c_char_p,
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


