from textual.widgets import DataTable


class ListView(DataTable):
    def __init__(self, list):
        super().__init__()
        self.headers = list.headers

    def on_mount(self):
        self.add_columns(*self.headers)
