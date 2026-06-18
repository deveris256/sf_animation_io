import ctypes

import bpy

import CommonUtils
from API.AnimConverterFunc import (
    _GetAnimationBlockC, _GetScalarSqSizeC, _GetScalarFromSqC,
    _GetFrameFromScalarFrameC, _GetTranslationSqSizeC, _GetTranslationFromSqC, _GetFrameFromTranslationFrameC,
    _GetRotationSqSizeC, _GetRotationFromSqC, _GetFrameFromRotationFrameC,
)
from API.AnimFrameData import AnimFrameData
from API.RigUtils import correct_bone_axis
from API.SkeletonRig import SkelRig


class AnimData():
    def __init__(self):
        self.frames = {}
        self.name = "UNKNOWN ANIMATION"
        self.start = 0
        self.end = 1

    def set_animation_data_attr(self, armature_obj):
        """Sets Blender armature attributes"""
        armature_obj.sf_anim_props.anim_name = self.name

    def LoadAnimationAttributes(self, armature_obj):
        """Loads data from Blender armature"""
        self.name = armature_obj.sf_anim_props.anim_name

    def GetFrameCount(self):
        """Gets animation frame count"""
        return len(list(self.frames.keys()))

    def GetFrame(self, frame_number):
        """Gets specific frame"""
        str_frame_number = str(frame_number)
        if str_frame_number not in self.frames:
            return None
        return self.frames[str_frame_number]

    def AddGetFrame(self, frame_number):
        """Gets frame or adds a new one, always returns a frame"""
        frame = self.GetFrame(frame_number)

        str_frame_number = str(frame_number)
        if frame == None:
            self.frames.update({str_frame_number: AnimFrameData()})

        return self.frames[str_frame_number]

    # whatever that is
    #def GetBoneList(self):
    #    bones = []
    #    for frame in self.frames:
    #        for bdata in frame.bone_data:
    #            bones.append(bdata.bone_name)
    #    return bones

    def load_from_ptr(self, anim_ptr : ctypes.c_void_p, rig : SkelRig):
        """Loads animation from pointer"""
        self.start = 0
        print("Loading animation from pointer...")
        print(anim_ptr)
        #self.name = _GetAnimationTitleC(anim_ptr).decode('utf-8')

        #animBlockCount = _GetAnimationBlockCountC(anim_ptr)

        for bone in rig.bones:
            name = bone.bone_name

            anim_block = _GetAnimationBlockC(
                anim_ptr,
                name.encode('utf-8')
            )

            #name = _GetAnimBlockBoneNameC(animBlock).decode('utf-8').strip()

            sqs_size = _GetScalarSqSizeC(anim_block)
            for s in range(sqs_size):
                sqs = _GetScalarFromSqC(anim_block, s)
                frame = str(_GetFrameFromScalarFrameC(sqs))
                frame_data = self.AddGetFrame(frame)
                bone_data_idx = frame_data.add_get_bone_index_by_name(name)
                frame_data.bone_data[bone_data_idx].scale.PtrSetScale(sqs)

            tsq_size = _GetTranslationSqSizeC(anim_block)
            for t in range(tsq_size):
                tsq = _GetTranslationFromSqC(anim_block, t)
                frame = str(_GetFrameFromTranslationFrameC(tsq))
                frame_data = self.AddGetFrame(frame)

                bone_data_idx = frame_data.add_get_bone_index_by_name(name)
                frame_data.bone_data[bone_data_idx].translation.PtrSetTranslation(tsq)

            rsq_size = _GetRotationSqSizeC(anim_block)
            for r in range(rsq_size):
                rsq = _GetRotationFromSqC(anim_block, r)
                frame = str(_GetFrameFromRotationFrameC(rsq))
                frame_data = self.AddGetFrame(frame)

                bone_data_idx = frame_data.add_get_bone_index_by_name(name)
                frame_data.bone_data[bone_data_idx].rotation.PtrSetRotation(rsq)
        #for _, frame in self.frames.items():
        #    for bone in frame.bone_data:
        #        mat = bone.get_matrix()
        #        bone.set_from_matrix(correct_bone_axis(mat))
        self.end = self.GetFrameCount()

    def LoadFromBlender(self, armature):
        """Loads animation from Blender armature"""
        if CommonUtils.GetBlenderVersion()[0] == 5:
            from bpy_extras import anim_utils

        self.LoadAnimationAttributes(armature)
        self.frames.clear()
        num_anim_frames = 0

        action = armature.animation_data.action

        if CommonUtils.GetBlenderVersion()[0] == 5:
            slot = action.slots[0] # for now
            channelbag = anim_utils.action_get_channelbag_for_slot(action, slot)

            for fcurve in channelbag.fcurves:
                for kp in fcurve.keyframe_points:
                    frame_num = int(kp.co[0])
                    num_anim_frames = max(frame_num, num_anim_frames)
        else:
            for fcurve in action.fcurves:
                for kp in fcurve.keyframe_points:
                    frame_num = int(kp.co[0])
                    num_anim_frames = max(frame_num, num_anim_frames)

        num_anim_frames += 1

        for frame_num in range(0, num_anim_frames, 1):
            frame = self.AddGetFrame(frame_num)
            bpy.context.scene.frame_set(frame_num)

            depsgraph = bpy.context.evaluated_depsgraph_get()
            depsgraph.update()
            armature = armature.evaluated_get(depsgraph)

            for pose_bone in armature.pose.bones:
                bone_name = pose_bone.name
                bone = frame.bone_data[frame.add_get_bone_index_by_name(bone_name)]
                bone.load_from_blender(pose_bone, armature)
