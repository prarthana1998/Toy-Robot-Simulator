class Table:
    """
    Represents the table with suitable height and width
    """
    def __init__(self, width, height):
        """
        Initialises the table with suitable width and height
        """
        self.width = width
        self.height = height

    def is_valid_position(self, x, y):
        """
        Checks if the position of the robot(x,y) is within the boundaries of the table
        """
        if 0 <= x < self.width and 0 <= y < self.height:
            return True
        return False