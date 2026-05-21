import mathutils

from API.AnimationBone import AnimBoneData

flip_x = mathutils.Matrix.Scale(-1, 4, (0, 1, 0))
sca = mathutils.Matrix.Scale(1.000, 4, [1.0, 1.0, 1.0])

already_processed = []


class AnimFrameData():
    def __init__(self):
        self.bone_data = []

    def GetBoneDataByName(self, bone_name):
        for bdata in self.bone_data:
            if bdata.bone_name == bone_name:
                return self.bone_data.index(bdata)
        return None

    def AddGetBoneIndexBoneName(self, bone_name):
        b = self.GetBoneDataByName(bone_name)
        if b != None:
            return b

        anim_bone = AnimBoneData()
        anim_bone.bone_name = bone_name

        self.bone_data.append(anim_bone)

        return self.bone_data.index(self.bone_data[-1])


