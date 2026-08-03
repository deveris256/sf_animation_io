import bpy



class SfAnimProperties(bpy.types.PropertyGroup):
    is_anim: bpy.props.BoolProperty(name="Is animation", default=False)
    anim_name: bpy.props.StringProperty(name="Name", default="UNKNOWN")
    validation_errors: bpy.props.StringProperty(name="Errors", default="")

_classes_ = [
    SfAnimProperties
]

def register():
    for c in _classes_: bpy.utils.register_class(c)

    o = bpy.types.Object
    o.sf_anim_props = bpy.props.PointerProperty(
        name="Starfield animation properties",
        type=SfAnimProperties
    )

def unregister():
    for c in _classes_: bpy.utils.unregister_class(c)

    o = bpy.types.Object
    del o.sf_anim_props
