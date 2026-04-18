from textual.app import App, ComposeResult

from .tracker import Model
from .view import HomeScreen


# from .view import View


class Controller(App):
    CSS_PATH = "style.tcss"
    BINDINGS = [
        ("d", "toggle_dark", "Toggle dark mode"),
        ("c", "create_list", "Create new TODO list"),
    ]
    SCREENS = {"HomeScreen": HomeScreen}

    def __init__(self):
        super().__init__()
        self.model = Model()

    def on_mount(self) -> ComposeResult:
        self.push_screen(HomeScreen(self.model.lists))

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.theme = (
            "textual-dark" if self.theme == "textual-light" else "textual-light"
        )

    def action_create_list(self):
        print("hello")
