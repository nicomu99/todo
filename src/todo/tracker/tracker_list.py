class TrackerList:
    # contains a list of ListEntries
    # what properties each ListEntry has
    # and maybe metadata
    def __init__(
        self,
        name: str
    ):
        self.name = name
        self.headers = ("id", "name", "description")
