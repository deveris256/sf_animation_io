import ctypes

from API import AnimConverter
from API.Animation import AnimData
from API.AnimConverterFunc import (
    _LoadAnimationSceneFromSFBGSFormatC, _list_to_wchar_arr, _GetSkeletonRigBoneCountC, _GetAnimationCountC,
    _GetAnimationSceneNameC, _GetAnimationWithIndexC, _CreateAnimationSceneC, _AddRigToAnimationSceneC,
    _CreateAnimationC, _CreateAnimBlockC, _LoadSFBGSSkeletonRigFromFileC, _AddAnimBlockToAnimationC
)
from API.SkeletonRig import SkelRig


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

    def GetAnimationPtr(self, bl_rig, rig_ptr, anim_index):
        """
        Constructs Animation Pointer
        """
        boneCount = _GetSkeletonRigBoneCountC(rig_ptr)
        animScenePtr = _CreateAnimationSceneC(self.name.encode('utf-8'))
        _AddRigToAnimationSceneC(animScenePtr, rig_ptr)

        animPtr = _CreateAnimationC(
            self.animations[anim_index].name.encode('utf-8'),
            boneCount
        )

        for rigBone in bl_rig.bones:
            if rigBone.bone_type_blender == "Twist":
                print(f"Skipped {rigBone.bone_name} animation data, as its type is Twist")
                continue

            animBlockPtr = _CreateAnimBlockC(rigBone.bone_name.encode('utf-8'))

            block_has_data = False

            for frameIdx, frameData in self.animations[anim_index].frames.items():
                frameIdx = int(frameIdx)
                internal_bone_idx = frameData.get_bone_data_by_name(rigBone.bone_name)  # Unrelated to actual idx
                if internal_bone_idx is None: continue  # Bone data is not present in frame, so is None
                frameBone = frameData.bone_data[internal_bone_idx]

                frameBone.AddDataToBlockPtr(frameIdx, animBlockPtr)

            #if block_has_data:

            _AddAnimBlockToAnimationC(
                animPtr,
                animBlockPtr,
                ctypes.c_bool(True),
            )
            print("Added block")

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
        )
        animCount = _GetAnimationCountC(animScene)

        self.name = _GetAnimationSceneNameC(animScene).decode('utf-8')

        rig_ptr = _LoadSFBGSSkeletonRigFromFileC(rig_path)
        rig = SkelRig()
        rig.from_ptr(rig_ptr, rig_path)

        for idx in range(animCount):
            anim_ptr = _GetAnimationWithIndexC(
                animScene,
                idx,
            )

            anim_data = AnimData()
            anim_data.load_from_ptr(anim_ptr, rig)

            self.AddAnimation(anim_data)


    def AddAnimation(self, data):
        if not isinstance(data, AnimData):
            raise TypeError(f"Data is not AnimData. Type of data: {type(data)}")

        self.animations.append(data)

    def AddNewAnimationFromBlender(self, rig_obj):
        animData = AnimData()
        animData.LoadFromBlender(rig_obj)
        self.AddAnimation(animData)

    def correct_with_registered_rig(self, rig, registered_rig):
        """
        Transforms animation and rig to correspond with registered rig.
        """

        # should NOT be used.
        #def process_frame_bone(frame_data, c):
            #frame_bone = [b for b in frame_data.bone_data if b.bone_name == c.bone_name]
            #if len(frame_bone) == 0:
            #    print(f"Skipping {c.bone_name}")
            #    return False
            #frame_bone = frame_bone[0]
            #t_reg_bone_mat = registered_rig.get_bone_by_name(
            #    frame_bone.bone_name).get_matrix()
            #t_bone_mat = rig.get_bone_by_name(
            #    frame_bone.bone_name).get_matrix()
            #t_delta_mat = t_reg_bone_mat @ t_bone_mat.inverted()
            #frame_bone_mat = frame_bone.get_matrix()
            #frame_bone.set_from_matrix(t_delta_mat @ frame_bone_mat)
            #return True

        def process_anim_bones_recursive(parent_bone):
            bl_rig_child_bones = [b for b in rig.bones if b.parent_name == parent_bone.bone_name]
            if len(bl_rig_child_bones) == 0: return

            for c in bl_rig_child_bones:
                #for anim in self.animations:
                #    for _, frame_data in anim.frames.items():
                #        process_frame_bone(frame_data, c)

                children = [b for b in rig.bones if b.parent_name == c.bone_name]

                for inner_c in children:
                    process_anim_bones_recursive(inner_c)


        temp1 = set([b.bone_name for b in rig.bones])
        temp2 = set([b.bone_name for b in registered_rig.bones])
        if len(temp1 - temp2) != 0:
            raise Exception(f"Registered rig and blender rig don't match in bones: {temp1 - temp2}")

        process_anim_bones_recursive(rig.bones[0])

        for bone in rig.bones:
            reg_rig_bone = registered_rig.get_bone_by_name(bone.bone_name)
            reg_mat = reg_rig_bone.get_matrix()
            bone_mat = bone.get_matrix()
            delta_mat = reg_mat @ bone_mat.inverted()

            bone.set_from_matrix(delta_mat @ bone_mat)
