from .properties import PropertyType


class ColumnProperty:
    # a property must have a type (date, string, number, select, status)
    def __init__(self, name: str, property_type: PropertyType, required: bool):
        self.name = name
        self.property_type = property_type
        self.required = required
