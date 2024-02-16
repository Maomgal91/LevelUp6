from unittest import TestCase
from levelup.character import Character

class TestCharacterInitWithName(TestCase):
    def test_init(self):
        ARBITRARY_NAME = "Bob"
        testobj = Character(ARBITRARY_NAME)
        self.assertEqual(ARBITRARY_NAME, testobj.name)

class TestCharacterMove(TestCase):
    def test_move(self):
        self.direction = "n"
        
        testobj = Character("Bob")
        testobj.move(self.direction)
        self.assertEqual(self.direction,testobj.direction)