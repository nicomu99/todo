from .property_type import PropertyType


class SelectProperty(PropertyType):
    def __init__(self, values: list[str]):
        super().__init__()
        self.values = values
