import unittest
from src.robot import Robot
from src.table import Table

class TestRotations(unittest.TestCase):
    def setUp(self):
        self.table = Table(5, 5)
        self.robot = Robot(self.table)

    def test_left(self):
        self.robot.place(0, 0, 'NORTH')
        self.robot.left()
        self.assertEqual(self.robot.facing, 'WEST')
        self.robot.left()
        self.assertEqual(self.robot.facing, 'SOUTH')
        self.robot.left()
        self.assertEqual(self.robot.facing, 'EAST')
        self.robot.left()
        self.assertEqual(self.robot.facing, 'NORTH')

    def test_right(self):
        self.robot.place(0, 0, 'NORTH')
        self.robot.right()
        self.assertEqual(self.robot.facing, 'EAST')
        self.robot.right()
        self.assertEqual(self.robot.facing, 'SOUTH')
        self.robot.right()
        self.assertEqual(self.robot.facing, 'WEST')
        self.robot.right()
        self.assertEqual(self.robot.facing, 'NORTH')

if __name__ == '__main__':
    unittest.main()
