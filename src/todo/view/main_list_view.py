from textual.app import ComposeResult
from textual.containers import HorizontalGroup, Center
from textual.widgets import Static, Button


class MainListView(HorizontalGroup):
    def __init__(self, name: str):
        super().__init__(name=name)
        # self.can_focus = True

    def compose(self) -> ComposeResult:
        yield Center(Static(self.name, classes="heading"))
        yield Button("Open", variant="success", id="update")
