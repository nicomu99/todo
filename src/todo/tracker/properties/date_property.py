from property_type import PropertyType


class DateProperty(PropertyType):
    def __init__(self, datetime):
        super().__init__()
        self.datetime = datetime
