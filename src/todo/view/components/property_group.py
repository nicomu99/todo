from textual.containers import HorizontalGroup
from textual.widgets import Static, Input


class PropertyGroup(HorizontalGroup):
    def __init__(self, list_property):
        super().__init__()
        self.list_property = list_property

    def compose(self):
        yield VerticalGroup(list_property.name)
