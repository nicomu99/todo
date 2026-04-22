from .column_property import ColumnProperty
from .list_entry import ListEntry


class TrackerList:
    # contains a list of ListEntries
    # what properties each ListEntry has
    # and maybe metadata
    def __init__(
        self,
        name: str,
        columns: list[ColumnProperty] | None = None,
        entries: ListEntry | None = None
    ):
        self.name = name
        self.columns = columns
        self.entries = entries  # contains
