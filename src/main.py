import json
from commands import process_commands
from utils import read_commands_from_file

def load_config(file_path):
    with open(file_path, 'r') as f:
        config = json.load(f)
    return config

def main():
    config = load_config('../config/config.json')
    commands_file = config.get('commands_file')
    
    if commands_file:
        commands = read_commands_from_file(commands_file)
        process_commands(commands)
    else:
        print("Error: Commands file path not specified in config.json")

if __name__ == "__main__":
    main()

