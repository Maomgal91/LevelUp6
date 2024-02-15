from levelup.position import Position

class Character:
    name = ""
    def __init__(self, character_name):
        self.name = character_name

    def move(self, direction):
        self.direction = direction
        if direction == 'n':
            pass