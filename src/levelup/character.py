class Character:
    name = ""
    direction = " "
    def __init__(self, character_name):
        self.name = character_name
        self.direction = ""
    def move(self, direction):
         self.direction = "n"
           