import bpy
import traceback

def ensure_bl_mode_on_obj(mode, obj):
    """
    Sets mode on object safely and guarantees the mode being set!
    """
    deselect_all_objects_set_active(obj)

    if bpy.context.mode != "OBJECT":
        bpy.ops.object.mode_set(mode="OBJECT")

    if bpy.context.mode != mode:
        bpy.ops.object.mode_set(mode=mode)

def ensure_object_mode():
    if bpy.context.mode != "OBJECT":
        bpy.ops.object.mode_set(mode="OBJECT")

def deselect_all_objects_set_active(active):
    [o.select_set(False) for o in bpy.data.objects if o != active]
    bpy.context.view_layer.objects.active = active

def deselect_all_objects():
    [o.select_set(False) for o in bpy.data.objects]

class SomethingHappenedException(Exception):
    def __init__(self, message="Uh-oh, something happened"):
        super().__init__(message)

def worked(func, args):
    try:
        func(*args)
    except Exception as e:
        return f"Error:\n {traceback.format_exc()}\n Actually:\n {str(e)}"
    return None

def spawn_error(self, error):
    error = f"Look, an error! Report to devs. Here's the error message:\n{error}"
    self.report({'ERROR'}, error)
