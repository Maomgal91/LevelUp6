from unittest import TestCase
from levelup.character import Position

class TestPositionInit(TestCase):
    def test_init(self):
        test_x = 5
        test_y = 5
        testobj = Position(test_x,test_y)
        self.assertEqual([5,5], testobj.Position)
