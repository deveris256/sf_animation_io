from API.AnimationIOWrappers import AnimFrameData
import bpy

class AnimData():
    def __init__(self):
        self.frames = {}
        self.name = "UNKNOWN ANIMATION"
        self.start = 0
        self.end = 1

    def SetAnimationAttributes(self, armature_obj):
        armature_obj.sf_anim_props.anim_name = self.name

    def LoadAnimationAttributes(self, armature_obj):
        self.name = armature_obj.sf_anim_props.anim_name

    def GetFrameCount(self):
        return len(list(self.frames.keys()))

    def GetFrame(self, frame_number):
        str_frame_number = str(frame_number)
        if str_frame_number not in self.frames:
            return None
        return self.frames[str_frame_number]

    def AddGetFrame(self, frame_number):
        frame = self.GetFrame(frame_number)

        str_frame_number = str(frame_number)
        if frame == None:
            self.frames.update({str_frame_number: AnimFrameData()})

        return self.frames[str_frame_number]

    def GetBoneList(self):
        bones = []
        for frame in self.frames:
            for bdata in frame.bone_data:
                bones.append(bdata.bone_name)
        return bones

    def LoadFromBlender(self, armature, rig_name_id_mapping):
        self.LoadAnimationAttributes(armature)
        self.frames.clear()
        num_anim_frames = 0

        action = armature.animation_data.action

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

                M = armature.convert_space(
                    pose_bone=pose_bone,
                    matrix=pose_bone.matrix,
                    from_space='POSE',
                    to_space='LOCAL',
                ).decompose()

                translation = M[0]
                rotation = M[1]
                scale = M[2]

                bone = frame.bone_data[frame.AddGetBoneIndexBoneName(bone_name)]
                bone.translation.blender = translation
                bone.rotation.blender_quaternion = rotation
                bone.scale.blender = scale

                #id
                bone.index = rig_name_id_mapping[bone.bone_name]
