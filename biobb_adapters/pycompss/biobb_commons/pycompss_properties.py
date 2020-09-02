
properties = None

def set_properties ( props ):
    global properties
    properties = props

def get_property ( key, sub_key = None, default_value = None):
    global properties
    if properties :
       group_prop = properties.get(key, None)
       if sub_key :
           if group_prop :
               return group_prop.get(sub_key, default_value)
    return default_value   
