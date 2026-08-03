import math

import bpy
from mathutils import Matrix

from CommonUtils import (
    ensure_object_mode)

class RigToNodes(bpy.types.Operator):
    bl_idname = "scene.convert_rig_to_nodes"
    bl_label = "Rig to empties node"

    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        active_obj = bpy.context.view_layer.objects.active
        if active_obj.type != "ARMATURE":
            return False
        return True

    def execute(self, context):
        rig = bpy.context.view_layer.objects.active

        ensure_object_mode()
        empties = []
        root_empty = None

        for bone in rig.data.bones:
            if bone.name in [n.name for n in bpy.data.objects]:
                raise Exception(f"Empty named {bone.name} already exists")

        for bone in rig.data.bones:
            empties.append(bpy.data.objects.new(bone.name, None))

        for bone in rig.data.bones:
            empty = [e for e in empties if e.name == bone.name][0]

            if bone.parent:
                empty_parent = [e for e in empties if e.name == bone.parent.name][0]
                empty.parent = empty_parent
            else:
                root_empty = empty

            #loc_mod = empty.constraints.new("COPY_LOCATION")
            #rot_mod = empty.constraints.new("COPY_ROTATION")

            #rot_mod.target = rig
            #loc_mod.target = rig
#
            #rot_mod.subtarget = bone.name
            #loc_mod.subtarget = bone.name

        for empty in empties:
            bpy.context.collection.objects.link(empty)

        for bone in rig.data.bones:
            empty = [e for e in empties if e.name == bone.name][0]
            bone_world = rig.matrix_world @ bone.matrix_local
            empty.matrix_world = bone_world
            empty.empty_display_size = bone.length


        return {'FINISHED'}

_classes = [
RigToNodes,
]

def menu_func_rig_to_empties(self, context):
    self.layout.operator(
        RigToNodes.bl_idname,
        text="Rig to Empties Nodes",
    )

def register():
    for c in _classes:
        bpy.utils.register_class(c)

    bpy.types.VIEW3D_MT_view.append(menu_func_rig_to_empties)

def unregister():
    for c in _classes:
        bpy.utils.unregister_class(c)

    bpy.types.VIEW3D_MT_view.remove(menu_func_rig_to_empties)
