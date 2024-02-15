from unittest import TestCase
from levelup.position import Position

class TestPositionInit(TestCase):
    def test_init(self):
        test_x = 5
        test_y = 5
        testposition = Position(test_x,test_y)
        self.assertEquals(test_x,testposition.x)
        self.assertEquals(test_y,testposition.y)