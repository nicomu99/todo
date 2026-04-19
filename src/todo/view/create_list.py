from textual.app import ComposeResult
from textual.screen import Screen
from textual.containers import VerticalGroup
from textual.widgets import Footer, Header, Static, Input


class CreateListScreen(Screen):
    BINDINGS = [
        ("a", "add_property", "Add Property"),
        ("escape", "escape_or_back", "Unfocus Input / Go Back")
    ]

    def __init__(self):
        super().__init__()
        self.properties = []

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        yield VerticalGroup(
            Static("List Name: ", classes="box"),
            Input(placeholder="...", classes="box"),
            classes="text-input-wrapper"
        )
        yield Static("Properties: ")
        for property in self.properties:
            yield PropertyGroup(property)

    def action_escape_or_back(self):
        if isinstance(self.focused, Input):
            self.set_focus(None)
        else:
            self.app.pop_screen()

    def action_add_property(self):
        pass
