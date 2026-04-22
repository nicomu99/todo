class ListEntry:
    # each entry has a unique id
    # and properties that are defined list-wise
    def __init__(self, list_id: int, entries: dict[str, str]):
        self.list_id = list_id
        self.entries = entries
