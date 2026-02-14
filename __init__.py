class StringCombineX:
    INPUT_COUNT = 10

    @classmethod
    def INPUT_TYPES(cls):
        DEF_ATTR_IN = {"default": "", "forceInput": True}
        DEF_ATTR_SFX = {"default": ""}
        optional_inputs = {}
        optional_inputs["prefix"] = ("STRING", {**DEF_ATTR_SFX})
        for i in range(1, cls.INPUT_COUNT + 1):
            optional_inputs[f"input{i}"] = ("STRING", {**DEF_ATTR_IN})
            optional_inputs[f"suffix{i}"] = ("STRING", {**DEF_ATTR_SFX})

        return {
            "required": {},
            "optional": optional_inputs
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("string",)
    CATEGORY = "utils/string"
    FUNCTION = "execute"
    DESCRIPTION = (
        "Combine strings with suffixes. Prefix is prepended to the final output. "
        "Change INPUT_COUNT in the class to adjust the number of input pairs."
    )

    def execute(self, prefix: str = "", **kwargs):
        parts = []

        for i in range(1, self.INPUT_COUNT + 1):
            input_val = kwargs.get(f"input{i}", "")
            suffix_val = kwargs.get(f"suffix{i}", "")
            s = "" if input_val is None else str(input_val)
            d = "" if suffix_val is None else str(suffix_val)
            if s:
                parts.append(s)
                if d:
                    parts.append(d)

        prefix = "" if prefix is None else str(prefix)
        combined = "".join([prefix] + parts)
        return (combined,)
    
#class StringCombine5(StringCombineX):
#    INPUT_COUNT = 5

class StringCombine10(StringCombineX):
    INPUT_COUNT = 10    
    

NODE_CLASS_MAPPINGS = {
#    "StringCombine5": StringCombine5,    
    "StringCombine10": StringCombine10,
}

NODE_DISPLAY_NAME_MAPPINGS = {
#    "StringCombine5": "String Combine 5",    
    "StringCombine10": "String Combine 10",
}