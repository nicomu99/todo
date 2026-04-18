from textual.app import App, ComposeResult
from textual.containers import Container, VerticalScroll
from textual.widgets import Footer, Header

from .tracker import Model
from .view import ListView, MainListView

# from .view import View


class Controller(App):
    CSS_PATH = "style.tcss"
    BINDINGS = [
        ("d", "toggle_dark", "Toggle dark mode"),
        ("c", "create_list", "Create new TODO list"),
    ]

    def __init__(self):
        super().__init__()
        self.model = Model()

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        with VerticalScroll(id="container"):
            for list in self.model.lists:
                yield MainListView(list.name)

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.theme = (
            "textual-dark" if self.theme == "textual-light" else "textual-light"
        )

    def action_create_list(self):
        print("hello")
