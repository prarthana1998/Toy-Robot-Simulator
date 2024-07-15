import unittest
from src.robot import Robot
from src.table import Table

class TestRobot(unittest.TestCase):
    def setUp(self):
        self.table = Table(5, 5)
        self.robot = Robot(self.table)

    def test_place_invalid_x_y(self):
        self.robot.place('a', 0, 'NORTH')
        self.assertEqual((self.robot.x, self.robot.y, self.robot.facing), (None, None, None))

        self.robot.place(0, 'b', 'NORTH')
        self.assertEqual((self.robot.x, self.robot.y, self.robot.facing), (None, None, None))

    def test_place_valid(self):
        self.robot.place(0, 0, 'NORTH')
        self.assertEqual((self.robot.x, self.robot.y, self.robot.facing), (0, 0, 'NORTH'))

    def test_place_invalid(self):
        self.robot.place(5, 5, 'NORTH')
        self.assertIsNone(self.robot.x)
        self.assertIsNone(self.robot.y)
        self.assertIsNone(self.robot.facing)

    def test_move_within_bounds(self):
        self.robot.place(0, 0, 'NORTH')
        self.robot.move()
        self.assertEqual((self.robot.x, self.robot.y), (0, 1))

    def test_move_out_of_bounds(self):
        self.robot.place(4, 4, 'NORTH')
        self.robot.move()
        self.assertEqual((self.robot.x, self.robot.y), (4, 4))

    def test_left_turn(self):
        self.robot.place(0, 0, 'NORTH')
        self.robot.left()
        self.assertEqual(self.robot.facing, 'WEST')

    def test_right_turn(self):
        self.robot.place(0, 0, 'NORTH')
        self.robot.right()
        self.assertEqual(self.robot.facing, 'EAST')

    def test_report(self):
        self.robot.place(1, 2, 'EAST')
        self.assertEqual(self.robot.report(), '1,2,EAST')

    def test_ignore_invalid_commands(self):
        self.robot.move()
        self.assertIsNone(self.robot.x)
        self.assertIsNone(self.robot.y)
        self.assertIsNone(self.robot.facing)

    def test_ignore_commands_until_valid_place(self):
        self.robot.left()
        self.robot.right()
        self.robot.move()
        self.robot.report()
        self.assertIsNone(self.robot.x)
        self.assertIsNone(self.robot.y)
        self.assertIsNone(self.robot.facing)
        self.robot.place(1, 2, 'EAST')
        self.assertEqual((self.robot.x, self.robot.y, self.robot.facing), (1, 2, 'EAST'))

if __name__ == '__main__':
    unittest.main()
