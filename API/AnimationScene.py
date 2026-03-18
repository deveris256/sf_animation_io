import ctypes

from API import AnimConverter
from API.AnimConverterFunc import _GetSkeletonRigBoneCountC, _CreateAnimationSceneC, _AddRigToAnimationSceneC, \
    _CreateAnimationC, _CreateAnimBlockC, _ExecuteRDPReduction_ScalarC, _ExecuteRDPReduction_TranslationC, \
    _ExecuteRDPReduction_RotationC, _AddAnimBlockToAnimationC, _LoadAnimationSceneFromSFBGSFormatC, _list_to_wchar_arr, \
    _GetAnimationCountC, _GetAnimationSceneNameC, _GetAnimationC, _GetAnimationTitleC, _GetAnimationBlockCountC, \
    _GetAnimationBlockC, _GetAnimBlockBoneNameC, _GetScalarSqSizeC, _GetScalarFromSqC, _GetFrameFromScalarEntryC, \
    _GetTranslationSqSizeC, _GetTranslationFromSqC, _GetRotationSqSizeC, _GetFrameFromRotationEntryC, \
    _GetRotationFromSqC, _GetFrameFromTranslationEntryC
from API.Animation import AnimData


class AnimScene:
    def __init__(self):
        self.name = "UNKNOWN"
        self.animations = []

    def SetAnimationAttributes(self, armature_obj):
        """
        Marks current armature as animation
        and sets required attributes
        """
        armature_obj.sf_anim_props.is_anim = True
        armature_obj.sf_anim_props.anim_name = self.name

    def LoadAnimationAttributes(self, armature_obj):
        """
        Loads attributes from armature
        """
        #TODO: Check if armature is animation
        self.name = armature_obj.sf_anim_props.anim_name

    @property
    def anim_count(self):
        return len(self.animations)

    def GetAnimationPtr(self, rigData, rig_path, anim_index):
        """
        Constructs Animation Pointer
        """
        rig_ptr = AnimConverter.LoadRigPtr(rig_path)
        boneCount = _GetSkeletonRigBoneCountC(rig_ptr)
        animScenePtr = _CreateAnimationSceneC(self.name.encode('utf-8'))
        _AddRigToAnimationSceneC(animScenePtr, rig_ptr, ctypes.c_bool(False))

        animPtr = _CreateAnimationC(
            self.animations[anim_index].name.encode('utf-8'),
            boneCount
        )

        for rigBone in rigData.bones:
            bone_idx = rigBone.index

            if rigBone.bone_type_blender == "Twist":
                print(f"Skipped {rigBone.bone_name} animation data, as its type is Twist")
                continue

            animBlockPtr = _CreateAnimBlockC(
                rigBone.bone_name.encode('utf-8'),
                bone_idx,
                ctypes.c_bool(False))

            block_has_data = False

            for frameIdx, frameData in self.animations[anim_index].frames.items():
                frameIdx = int(frameIdx)
                internal_bone_idx = frameData.GetBoneDataByName(rigBone.bone_name)  # Unrelated to actual idx
                if internal_bone_idx is None: continue  # Bone data is not present in frame, so is None
                frameBone = frameData.bone_data[internal_bone_idx]

                block_has_data = frameBone.AddDataToBlockPtr(frameIdx, animBlockPtr)

            if block_has_data:

                _ExecuteRDPReduction_ScalarC(animBlockPtr, 0.0002)
                _ExecuteRDPReduction_TranslationC(animBlockPtr, 0.00025)
                _ExecuteRDPReduction_RotationC(animBlockPtr, 0.0000863)

                _AddAnimBlockToAnimationC(
                    animPtr,
                    animBlockPtr,
                    ctypes.c_bool(True),
                    ctypes.c_bool(False)
                )
            else:
                pass

        return animPtr

    def ConstructFromFile(self, input_path, rig_path):
        """
        Constructs AnimScene from file.
        """
        templist = [rig_path, input_path]
        wchars = _list_to_wchar_arr(templist)

        animScene = _LoadAnimationSceneFromSFBGSFormatC(
            wchars,
            len(templist),
            ctypes.c_bool(False)
        )
        animCount = _GetAnimationCountC(animScene)

        self.name = _GetAnimationSceneNameC(animScene).decode('utf-8')

        for idx in range(animCount):
            anim_data = AnimData()
            anim_data.start = 0

            anim = _GetAnimationC(
                animScene,
                idx,
                ctypes.c_bool(False)
            )

            anim_data.name = _GetAnimationTitleC(anim).decode('utf-8')

            animBlockCount = _GetAnimationBlockCountC(
                anim
            )

            for b_idx in range(animBlockCount):
                animBlock = _GetAnimationBlockC(
                    anim,
                    b_idx,
                    ctypes.c_bool(False)
                )

                name = _GetAnimBlockBoneNameC(animBlock).decode('utf-8').strip()

                sqs_size = _GetScalarSqSizeC(animBlock)
                for s in range(sqs_size):
                    sqs = _GetScalarFromSqC(animBlock, s, ctypes.c_bool(False))
                    frame = str(_GetFrameFromScalarEntryC(sqs))
                    frame_data = anim_data.AddGetFrame(frame)
                    bone_data_idx = frame_data.AddGetBoneIndexBoneName(name)
                    frame_data.bone_data[bone_data_idx].scale.PtrSetScale(sqs)

                tsq_size = _GetTranslationSqSizeC(animBlock)
                for t in range(tsq_size):
                    tsq = _GetTranslationFromSqC(animBlock, t, ctypes.c_bool(False))
                    frame = str(_GetFrameFromTranslationEntryC(tsq))
                    frame_data = anim_data.AddGetFrame(frame)
                    bone_data_idx = frame_data.AddGetBoneIndexBoneName(name)
                    frame_data.bone_data[bone_data_idx].translation.PtrSetTranslation(tsq)

                rsq_size = _GetRotationSqSizeC(animBlock)
                for r in range(rsq_size):
                    rsq = _GetRotationFromSqC(animBlock, r, ctypes.c_bool(False))
                    frame = str(_GetFrameFromRotationEntryC(rsq))
                    frame_data = anim_data.AddGetFrame(frame)
                    bone_data_idx = frame_data.AddGetBoneIndexBoneName(name)
                    frame_data.bone_data[bone_data_idx].rotation.PtrSetRotation(rsq)

            anim_data.end = anim_data.GetFrameCount()
            self.AddAnimation(anim_data)


    def AddAnimation(self, data):
        if not isinstance(data, AnimData):
            raise TypeError(f"Data is not AnimData. Type of data: {type(data)}")

        self.animations.append(data)

    def AddNewAnimationFromBlender(self, rig_obj, rigData):
        rig_name_id_mapping = {b.bone_name: b.index
                               for b in rigData.bones}
        animData = AnimData()
        animData.LoadFromBlender(rig_obj, rig_name_id_mapping)
        self.AddAnimation(animData)
