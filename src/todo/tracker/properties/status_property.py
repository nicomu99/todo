from .property_type import PropertyType


class StatusProperty(PropertyType):
    def __init__(self, statuses):
        super().__init__()
        self.statuses = statuses
