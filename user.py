class User:
    def __init__(self, username):
        self.username = username

    def to_db(self):
        pass

    @classmethod
    def from_db(cls):
        pass