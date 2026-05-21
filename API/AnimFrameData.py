from API.AnimationBone import AnimBoneData


class AnimFrameData():
    def __init__(self):
        self.bone_data = []

    def get_bone_data_by_name(self, bone_name):
        for bdata in self.bone_data:
            if bdata.bone_name == bone_name:
                return self.bone_data.index(bdata)
        return None

    def add_get_bone_index_by_name(self, bone_name):
        b = self.get_bone_data_by_name(bone_name)
        if b is not None:
            return b

        anim_bone = AnimBoneData()
        anim_bone.bone_name = bone_name

        self.bone_data.append(anim_bone)

        return self.bone_data.index(self.bone_data[-1])
