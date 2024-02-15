from unittest import TestCase
from levelup.character import Character

class TestCharacterInitWithName(TestCase):
    def test_init(self):
        ARBITRARY_NAME = "Bob"
        testobj = Character(ARBITRARY_NAME)
        selfc.assertEqual(ARBITRARY_NAME, testobj.name)
