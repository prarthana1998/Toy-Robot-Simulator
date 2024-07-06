import unittest
from src.robot import Robot
from src.table import Table

class TestRobot(unittest.TestCase):
    def setUp(self):
        self.table = Table(5, 5)
        self.robot = Robot(self.table)

    def test_place_and_report(self):
        self.robot.place(0, 0, 'NORTH')
        self.assertEqual(self.robot.report(), "0,0,NORTH")

    def test_move(self):
        self.robot.place(0, 0, 'NORTH')
        self.robot.move()
        self.assertEqual(self.robot.report(), "0,1,NORTH")

    def test_left(self):
        self.robot.place(0, 0, 'NORTH')
        self.robot.left()
        self.assertEqual(self.robot.report(), "0,0,WEST")

    def test_right(self):
        self.robot.place(0, 0, 'NORTH')
        self.robot.right()
        self.assertEqual(self.robot.report(), "0,0,EAST")

    def test_avoid_falling(self):
        self.robot.place(0, 0, 'SOUTH')
        self.robot.move()
        self.assertEqual(self.robot.report(), "0,0,SOUTH")

    def test_ignore_invalid_place(self):
        # Invalid placement should not change robot's state
        self.robot.place(0, 0, 'INVALID_DIRECTION')
        self.assertEqual(self.robot.report(), None)

if __name__ == "__main__":
    unittest.main()

