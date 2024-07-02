class GetListElementByIndex:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "list": ("LIST",),
                "index": ("INT", {"min": 0, "max": 20000, "default": 0})
            },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("element_str",)
    FUNCTION = "get_element"
    CATEGORY = f"Yunz"

    def get_element(self, list, index):
        return (str(list(index)),)


NODE_DISPLAY_NAME_MAPPINGS = {
    "GetListElementByIndex": "GetListElementByIndex",
}

NODE_CLASS_MAPPINGS = {
    key: globals()[key] for key in NODE_DISPLAY_NAME_MAPPINGS.keys()
}