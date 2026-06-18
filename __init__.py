import bpy
import os
import sys

dir = os.path.dirname(os.path.realpath(__file__))
if dir not in sys.path:
    sys.path.append(dir)

import CommonUtils
import AnimationOperators
import RigOperators

if CommonUtils.GetBlenderVersion()[0] != 5:
    # Modules
    import imp
    from API import (
        BlenderSpecificUtils,
        AnimConverterFunc,
        AnimConverter,
        AnimFrameData,
        RigBone,
        RigUtils,
        SkeletonRig,
        AnimationUtils,
        AnimationBone,
        AnimationScene,
        Animation,
    )
    imp.reload(BlenderSpecificUtils)
    imp.reload(AnimConverterFunc)
    imp.reload(AnimationScene)
    imp.reload(SkeletonRig)
    imp.reload(AnimConverter)
    imp.reload(CommonUtils)
    imp.reload(AnimationUtils)
    imp.reload(RigUtils)
    imp.reload(AnimFrameData)
    imp.reload(RigBone)
    imp.reload(Animation)
    imp.reload(AnimationBone)
    imp.reload(AnimationOperators)
    imp.reload(RigOperators)

bl_info = {
    "name": "Starfield Animation",
    "author": "Deveris, Calaverah & Jojo",
    "version": (1, 0, 0),
    "blender": (4, 3, 0),
    "location": "File > Import-Export",
    "description": "Export & Import Starfield .af & .rig",
    "warning": "",
    "category": "Import-Export",
}

__modules__ = [
    AnimationOperators,
    RigOperators
]

# Register the operators and menu entries
def register():
    for module in __modules__:
        module.register()

def unregister():
    for module in __modules__:
        module.unregister()

if __name__ == "__main__":
    register()
