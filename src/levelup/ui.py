import logging
from typing import Callable
from levelup.controller import GameController
from levelup.direction import Direction

VALID_DIRECTIONS = [x.value for x in Direction]
VALID_COMMANDS = VALID_DIRECTIONS + ["q"]


# This is prewritten for you. You should only have to change it to make the text copy match what your prompts should say
class GameApp:
    controller: GameController
    starting_pos = (-100, -100)

    def __init__(self):
        self.controller = GameController()

    def prompt(self, menu: str, validation_fn: Callable[[str], bool]) -> str:
        while True:
            response = input(f"\n{menu}\n> ")
            if validation_fn(response):
                break
            else:
                print(f"{response} is an invalid input. Try again.")
        return response

    def create_character(self):
        CHARACTERPROMPT = '''
            ,*-.
            |  |
        ,.  |  |   You wake up next to a large blooming saguaro
        | |_|  | ,.   as a stranger shakes you awake.
        `---.  |_| |
            |  .--`
            |  |      He asks for your name:
            |  |
'''
        #CHARACTERPROMPT = "You wake up on a sandy beach with a stranger shaking you awake. He asks for your name:"
        #character = self.prompt("Enter character name", lambda x: len(x) > 0)
        character = self.prompt(CHARACTERPROMPT, lambda x: len(x) > 0)
        self.controller.create_character(character)

        WELCOMEPROMPT = "You look around to see a desolate landscape as far as the eye can see. \nYou hear the strangers voice behind you, \n\"Welcome to the desert "
        #print(f"Welcome, {self.controller.status.character_name}")
        #print(f""WELCOMEPROMPT " " {self.controller.status.character_name}")
        print(f"{WELCOMEPROMPT}{self.controller.status.character_name}...\"")

    def move_loop(self):
        while True:
            response = self.prompt(
                f"Where would you like to go? {VALID_DIRECTIONS}\n(or q to quit this world)",
                lambda x: x in VALID_COMMANDS,
            )
            if response == "q":
                self.quit()
            direction = Direction(response)
            self.controller.move(direction)
            print(f"You moved {direction.name}")
            print(self.controller.status)

    def start(self):
        self.create_character()
        self.controller.start_game()
        self.starting_pos = self.controller.status.current_position
        self.move_loop()

    def quit(self):
        print(
            f"{self.controller.status.character_name} started on {self.starting_pos}, ended on {self.controller.status.current_position} and moved {self.controller.status.move_count} times."
        )
        quit()