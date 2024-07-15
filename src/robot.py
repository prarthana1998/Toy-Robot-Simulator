from table import Table
class Robot:
    """
    Represents that the robot can be placed, moved or rotated (left and right) on the table
    """
    DIRECTIONS = ['NORTH', 'EAST' , 'SOUTH', 'WEST']
    def __init__(self, table):
        """
        Initialises robot with reference to table and set configuration(x,y) and direction to None.
        """
        self.table = table
        self.x = None
        self.y = None
        self.facing = None

    def place(self, x, y, facing):
        """
        Places the robot in the specified position(x,y) and direction
        """
        if not isinstance(facing, str):
            print(f"Warning: 'facing' must be a string")
            return
        try:
            # Check if x and y can be converted to integers
            x = int(x)
            y = int(y)
        except ValueError:
            print(f"Warning: Invalid PLACE command with position ({x}, {y}) and facing '{facing}'")
            return
        
        if self.table.is_valid_position(x, y) and facing.upper() in self.DIRECTIONS:
            self.x = x
            self.y = y
            self.facing = facing.upper() # converting to uppercase for case-sensitivity

        else:
            print(f"Warning: Invalid PLACE command with position ({x}, {y}) and facing '{facing}'")

    def move(self):
        """
        Moves the robot one unit in the given direction provided the move is valid
        """
        if self.x is None or self.y is None or self.facing is None:
            return
        new_x, new_y = self.x, self.y

        if self.facing == 'NORTH':
            new_y += 1
        elif self.facing == 'EAST':
            new_x +=1
        elif self.facing == 'SOUTH':
            new_y -=1
        elif self.facing == 'WEST':
            new_x -=1

        # checking if the new position is valid
        if self.table.is_valid_position(new_x, new_y):
            self.x, self.y = new_x, new_y

    def left(self):
        """
        Represents the 90 degree rotation of the robot to the left
        """
        if self.facing is not None:
            current_index = self.DIRECTIONS.index(self.facing)
            self.facing = self.DIRECTIONS[(current_index - 1) % 4] # for the index to wrap in case it goes below 0
        
    def right(self):
        """
        Represents the 90 degree rotation of the robot to the right
        """
        if self.facing is not None:
            current_index = self.DIRECTIONS.index(self.facing)
            self.facing = self.DIRECTIONS[(current_index + 1) % 4] # for the index to wrap in case it goes above 0

    def report(self):
        """
        Gives the final output i.e x, y coordinates along with the dorection the robot is facing 
        """
        if self.x is not None and self.y is not None and self.facing is not None:
            return f"{self.x},{self.y},{self.facing}"
        return None