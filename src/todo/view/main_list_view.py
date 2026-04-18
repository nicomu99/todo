from textual.app import ComposeResult
from textual.containers import HorizontalGroup
from textual.widgets import Static


class MainListView(HorizontalGroup):
    def __init__(self, name: str):
        super().__init__()
        self.title = name

    def compose(self) -> ComposeResult:
        yield Static(self.title)
        yield
