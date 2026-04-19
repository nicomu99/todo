from textual.app import App

from .tracker import Model
from .view import HomeScreen, CreateListScreen


class Controller(App):
    CSS_PATH = "style.tcss"

    def __init__(self):
        super().__init__()
        self.model = Model()

    def on_mount(self):
        self.install_screen(HomeScreen(self.model.lists), name="home")
        self.install_screen(CreateListScreen(), name="create_list")
        self.push_screen("home")
