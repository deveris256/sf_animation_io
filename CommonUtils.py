import mathutils

def GenDescriptionBox(text_list, layout, scale=0.3):
    for text in text_list:
        row = layout.row()
        row.label(text=text)
        row.scale_y = scale
    return text_list

def PrepareFileName(s):
    s = s.strip().replace(" ", "_")
    return "".join(x for x in s if x.isalnum())

def GenPrettyPropTable(layout, obj, props_dict, space_for_icons=True):
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

def GenPrettyPropTableWithLabel(layout, obj, props_dict, space_for_icons=True):
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
