class Tracks():
    def __init__(self):
        self.titles = []

    def add(self, song):
        self.titles.append(song)

    def list(self):
        return self.titles