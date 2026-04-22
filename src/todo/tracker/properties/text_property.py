from .property_type import PropertyType


class TextProperty(PropertyType):
    def __init__(self, text: str):
        super().__init__()
        self.text = text
