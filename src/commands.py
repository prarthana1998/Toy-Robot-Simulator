from table import Table
from robot import Robot

def process_commands(commands):
    """
    Processes a list of commands to control the robot.
    """
    table = Table(5, 5)
    robot = Robot(table)

    for command in commands:
        command = command.replace("\u00A0", " ")  # Replace any non-breaking spaces with regular space.
        try:

            parts = command.split(maxsplit=1)
            if not parts:
                continue
            command_name = parts[0].upper()

            if command_name == "PLACE":
                if len(parts) == 2:
                    params = parts[1].split(',')
                    if len(params) == 3:
                        x, y , facing = map(str.strip, params) #Strip whitespace from each part.
                        robot.place(int(x), int(y), facing) #convert the strings representing the x and y coordinates into integers.
                    else:
                        print(f"Warning: Invalid command format: {command}")
                else:
                    print(f"Warning: Invalid command format: {command}")
                    
            elif command_name == "MOVE":
                robot.move()

            elif command_name == "LEFT":
                robot.left()

            elif command_name == "RIGHT":
                robot.right()

            elif command_name == "REPORT":
                report = robot.report()
                if report:
                    print(f"Output: {report}")
            
            else:
                print(f"Warning: Invalid command: {command}")

        except ValueError as ve:
            print(f"Error: {str(ve)}")
        except Exception as e:
            print(f"Error: {str(e)}")
