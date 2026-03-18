import os
import shutil

import mathutils

from API.AnimationUtils import BoneAxisCorrection_Alt, BoneAxisCorrectionInv, BoneAxisCorrection

def GetRigByName(name):
    path = os.path.join(GetRigFolder(), f"{name}.rig")
    if not os.path.isfile(path):
        return None
    return path

def GetRigFolder():
    rig_folder = os.path.join(os.path.dirname(__file__), "Assets", "Rigs")
    if not os.path.isdir(rig_folder):
        os.makedirs(rig_folder)

    return rig_folder

def GetExistingRigs():
    names = []
    with os.scandir(GetRigFolder()) as entries:
        for entry in entries:
            if not entry.name.lower().endswith(".rig"): continue
            names.append(entry.name[:-4])
    return names

def RegisterRigFile(rig_path, rig_name):
    source_path = rig_path
    destination_path = os.path.join(GetRigFolder(), f"{rig_name}.rig")
    shutil.copyfile(source_path, destination_path)

def RecursiveCreateRig(obj, rig_data, current_list=[]):
    edit_bones = obj.data.edit_bones
    bones = obj.data.bones

    for rig_bone in current_list:
        if edit_bones.get(rig_bone.bone_name) == None:
            pose_bone = edit_bones.new(name=rig_bone.bone_name)
        else:
            pose_bone = edit_bones.get(rig_bone.bone_name)

        rot = mathutils.Quaternion(rig_bone.rotation.raw_wxyz)#.to_euler()
        rot = rot.to_matrix().to_4x4()
        tra = mathutils.Matrix.Translation(rig_bone.translation)
        scale = mathutils.Matrix.Scale(1.000, 4, [1.0, 1.0, 1.0])
        
        pose_bone.length = 0.07
        pose_bone.roll = 0

        pose_bone.matrix = tra @ rot @ scale

        pose_bone["anim_bone_index"] = rig_bone.index

        if rig_bone.parent_name is not None:
            pose_bone.parent = edit_bones.get(rig_bone.parent_name)
            pose_bone.matrix = pose_bone.parent.matrix @ pose_bone.matrix

        cur_list = [
            b for b in rig_data.bones if b.bone_name not in [b.name for b in edit_bones] and
            b.parent_name == rig_bone.bone_name
        ]

        RecursiveCreateRig(obj, rig_data, current_list=cur_list)

def RigPostProcess(obj):
    """Expects edit mode."""
    for edit_bone in obj.data.edit_bones:
        edit_bone.matrix = BoneAxisCorrection_Alt(edit_bone.matrix)

def RigSetBoneAttr(rig, obj):
    """Expects edit mode."""
    for bone in obj.data.edit_bones:
        rig_bone = rig.GetBone(bone.name)
        rig_bone.SetArmatureBoneAttributes(bone)

def rig_list_enum_items(self, context):
    items = [(rig_name, rig_name, "") for rig_name in GetExistingRigs()]
    if len(items) == 0:
        items.append(("NONE", "NONE", "NO RIGS FOUND"))
    return items
