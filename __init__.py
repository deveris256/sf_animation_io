import bpy
import os
import sys

dir = os.path.dirname(os.path.realpath(__file__))
if dir not in sys.path:
	sys.path.append(dir)

# Modules
import AnimationOperators
import RigOperators

import imp
from API import (
    AnimConverterFunc,
    AnimConverter,
    AnimationIOWrappers,
    RigUtils,
    AnimationUtils,
    AnimationBone,
    AnimationScene,
    Animation
)
import CommonUtils
imp.reload(CommonUtils)
imp.reload(AnimationUtils)
imp.reload(RigUtils)
imp.reload(AnimConverterFunc)
imp.reload(AnimationIOWrappers)
imp.reload(Animation)
imp.reload(AnimationScene)
imp.reload(AnimationBone)
imp.reload(AnimConverter)
imp.reload(AnimationOperators)

imp.reload(RigOperators)

bl_info = {
	"name": "Starfield Animation",
	"author": "Deveris, Calaverah & Jojo",
	"version": (1, 0, 0),
	"blender": (4, 3, 0),
	"location": "File > Import-Export",
	"description": "Export & Import Starfield .af, and other animation-related files",
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
