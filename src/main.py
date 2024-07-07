import json
from commands import process_commands
from utils import read_commands_from_file

def load_config(file_path):
    """
    Loads the configuration from the json file.
    """
    with open(file_path, 'r') as f:
        config = json.load(f)
    return config

def main():
    """
    Main function to load configuration, read commands from file and process commands.
    """
    # Loading the config file
    config = load_config('../config/config.json')
    
    # Get the path of the input file from the config file
    commands_file = config.get('commands_file')
    
    if commands_file:
        # Read file from using the given method in utils file
        commands = read_commands_from_file(commands_file)

        #Process commands to control the robot
        process_commands(commands)
    else:
        print("Error: Commands file path not specified in config.json")

if __name__ == "__main__":
    main()

