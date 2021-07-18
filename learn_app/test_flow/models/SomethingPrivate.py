class SomethingPrivate:
    """Simulate some action that can be done only by user and admin"""

    def __init__(self, by_name, by_time):
        self.by_name = by_name
        self.by_time = by_time
