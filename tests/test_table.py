import unittest
from src.table import Table

class TestTable(unittest.TestCase):
    def setUp(self):
        self.table = Table(5, 5)

    def test_valid_positions(self):
        self.assertTrue(self.table.is_valid_position(0, 0))
        self.assertTrue(self.table.is_valid_position(4, 4))
        self.assertTrue(self.table.is_valid_position(2, 3))

    def test_invalid_positions(self):
        self.assertFalse(self.table.is_valid_position(-1, 2))
        self.assertFalse(self.table.is_valid_position(6, 3))
        self.assertFalse(self.table.is_valid_position(2, 6))
        self.assertFalse(self.table.is_valid_position(5, 5))

if __name__ == "__main__":
    unittest.main()
