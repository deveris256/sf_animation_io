bl_info = {
    "name": "Starfield Animation",
    "author": "Deveris, Calaverah & Jojo",
    "version": (2, 0, 0),
    "blender": (4, 3, 0),
    "location": "File > Import-Export",
    "description": "Export & Import Starfield .af & .rig",
    "warning": "",
    "category": "Import-Export",
}

import sys
import os

dir = os.path.dirname(os.path.realpath(__file__))
if dir not in sys.path:
    sys.path.append(dir)

import CommonUtilsAnimIO #0

from AnimationIO_bl import (
    RegisteredRigOP,
    RigProps,
    RigImportOP,
    RigExportOP,
    AnimationProps,
    AnimationImportOP,
    AnimationExportOP,
    RigToEmptiesOP,

    AnimationIOPanels, # last
)

if CommonUtilsAnimIO.get_blender_version()[0] != 5:
    # Modules
    import imp
    from AnimationIO import (
        AnimationIOFuncs,  #0
        BoneMatrix, #0
        AnimatedBone, #1
        AnimatableRig, #2
    )

    imp.reload(CommonUtilsAnimIO)

    imp.reload(AnimationIOFuncs)
    imp.reload(BoneMatrix)
    imp.reload(AnimatedBone)
    imp.reload(AnimatableRig)

    

    imp.reload(RegisteredRigOP)
    imp.reload(RigProps)
    imp.reload(RigImportOP)
    imp.reload(RigExportOP)
    imp.reload(AnimationProps)
    imp.reload(AnimationImportOP)
    imp.reload(AnimationExportOP)
    imp.reload(RigToEmptiesOP)
    imp.reload(AnimationIOPanels)

__modules__ = [
    RegisteredRigOP,
    RigProps,
    RigImportOP,
    RigExportOP,
    AnimationProps,
    AnimationImportOP,
    AnimationExportOP,
    RigToEmptiesOP,
    AnimationIOPanels,
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
