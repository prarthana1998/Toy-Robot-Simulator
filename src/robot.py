from table import Table

class Robot:
    """
    This functions gives a description about the commands that the robot is able to read.
    """
    DIRECTIONS = {"NORTH", "EAST" , "SOUTH", "WEST"}
    def __init__(self, table):
        self.table = table
        self.x = None
        self.y = None
        self.facing = None

    def place(self, x, y, facing):
        if self.table.is_valid_position(x,y) and facing.upper() in self.DIRECTIONS:
            self.x = x
            self.y = y
            self.facing = facing.upper()

