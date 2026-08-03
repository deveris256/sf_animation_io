import os

import bpy
import traceback
import textwrap

# todo: rename some of the methods to be lowercase

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
    print(error)
    self.report({'ERROR'}, error)

def gen_description_box(text_list, layout, scale=0.3):
    for text in text_list:
        row = layout.row()
        row.label(text=text)
        row.scale_y = scale
    return text_list

def prepare_file_name(s):
    s = s.strip().replace(" ", "_")
    return "".join(x for x in s if x.isalnum())

def gen_pretty_prop_table(layout, obj, props_dict, space_for_icons=True):
    for prop_name, prop_data in props_dict.items():
        prop_text = prop_data[0]
        prop_icon = prop_data[1]

        row = layout.row()
        row.scale_y = 0.85

        if prop_icon is None:
            row.label(text=prop_text)
            row.scale_x = 1.0

            row.prop(obj, prop_name, text="")
            row.scale_x = 0.1

            if space_for_icons:
                row.label(text="")
                row.scale_x = 1.1
        else:
            row.label(text=prop_text)
            row.scale_x = 1.0

            row.prop(obj, prop_name, text="")
            row.scale_x = 1.0

            row.label(text="", icon=prop_icon)
            row.scale_x = 1.1

def gen_pretty_prop_table_with_label(layout, obj, props_dict, space_for_icons=True):
    for prop_name, prop_data in props_dict.items():
        prop_text = prop_data[0]
        prop_evaluation_func = prop_data[1]
        prop_evaluation_args = prop_data[2]
        prop_icon = prop_data[3]

        row = layout.row()
        row.scale_y = 0.85

        if prop_icon is None:
            row.label(text=prop_text)
            row.scale_x = 1.0

            row.prop(obj, prop_name, text="")
            row.scale_x = 0.1

            if space_for_icons:
                row.label(text="")
                row.scale_x = 0.5
        else:
            row.label(text=prop_text)
            row.scale_x = 1.0

            row.prop(obj, prop_name, text="")
            row.scale_x = 1.0

            row.label(text="", icon=prop_icon)
            row.scale_x = 0.5

        row.scale_x = 1.0
        if prop_evaluation_func != None:
            text = prop_evaluation_func(getattr(obj, prop_name), **prop_evaluation_args)
            row.label(text=text)
        else:
            row.label(text="")

def get_blender_version():
    import bpy
    return bpy.app.version

def GetRigByName(name):
    path = os.path.join(GetRigFolder(), f"{name}.rig")
    if not os.path.isfile(path):
        return None
    return path

def GetRigReferenceObject(name):
    path = os.path.join(GetRigFolder(), f"{name}.fbx")
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

def rig_list_enum_items(self, context):
    items = [(rig_name, rig_name, "") for rig_name in GetExistingRigs()]
    if len(items) == 0:
        items.append(("NONE", "NONE", "NO RIGS FOUND"))
    return items

def gstr(strings):
    new_strings = {}
    for name, info in strings.items():
        info = info.strip().replace("\n", " ")
        info = textwrap.wrap(info, width=35)
        new_strings.update({name: info})
    return new_strings

def set_object_armature(mod_name, mesh_obj_name, armature_obj):
    mod_name = mod_name
    mesh_obj = bpy.context.scene.objects.get(mesh_obj_name)
    mods = [m for m in mesh_obj.modifiers if m.type == 'ARMATURE']

    if len(mods) == 0:
        modifier = mesh_obj.modifiers.new(name=mod_name, type='ARMATURE')
    else:
        modifier = mods[0]

    modifier.name = mod_name
    modifier.use_deform_preserve_volume = False
    modifier.use_multi_modifier = False
    modifier.object = armature_obj
    modifier.use_vertex_groups = True
    modifier.use_bone_envelopes = False
    mesh_obj.parent = armature_obj
