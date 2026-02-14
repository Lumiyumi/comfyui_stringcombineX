To install simply "git clone https://github.com/Lumiyumi/comfyui_stringcombineX.git" into your custom_nodes folder

to add different variations simply add classes at the bottom inheriting StringCombineX.

example:

class StringCombine10(StringCombineX):
    INPUT_COUNT = 10    

and add their values to the NODE_CLASS_MAPPINGS and NODE_DISPLAY_NAME_MAPPINGS.


left an example commented out. 
class StringCombine5(StringCombineX):
    INPUT_COUNT = 5
