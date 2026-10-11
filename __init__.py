import bpy

from . import CommonUtils
from . import AnimationOperators
from . import RigOperators

if CommonUtils.GetBlenderVersion()[0] != 5:
    # Modules
    import importlib
    from .API import (
        AnimConverterFunc,
        AnimConverter,
        AnimationIOWrappers,
        RigUtils,
        AnimationUtils,
        AnimationBone,
        AnimationScene,
        Animation
    )

    importlib.reload(CommonUtils)
    importlib.reload(AnimationUtils)
    importlib.reload(RigUtils)
    importlib.reload(AnimConverterFunc)
    importlib.reload(AnimationIOWrappers)
    importlib.reload(Animation)
    importlib.reload(AnimationScene)
    importlib.reload(AnimationBone)
    importlib.reload(AnimConverter)
    importlib.reload(AnimationOperators)

    importlib.reload(RigOperators)

bl_info = {
    "name": "Starfield Animation",
    "author": "Deveris, Calaverah & Jojo",
    "version": (1, 0, 1),
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
