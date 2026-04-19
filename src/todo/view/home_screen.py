from textual.app import ComposeResult
from textual.screen import Screen
from textual.containers import VerticalScroll
from textual.widgets import Footer, Header

from .main_list_view import MainListView


class HomeScreen(Screen):
    BINDINGS = [
        ("c", "create_list", "Create new TODO list"),
    ]

    def __init__(self, lists):
        super().__init__()
        self.show_lists = lists
        for show_list in self.show_lists:
            print(show_list.name)

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        with VerticalScroll(id="container"):
            for show_list in self.show_lists:
                yield MainListView(show_list.name)

    def action_create_list(self):
        self.app.push_screen("create_list")
