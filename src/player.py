# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, location):
        self.name = name
        self.location = location
    
    def __str__(self):
        return (f"{self.name}\n {self.location}")

    def move(self, direction):
        if hasattr(self.location, f"{direction}"):
            self.location = getattr(self.location, f"{direction}")
        if self.location is not None:
            self.location = self.location
        else:
            print("Please try a different direction")
