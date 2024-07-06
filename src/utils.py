def read_commands_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            commands = file.readlines()
        return commands
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return []
    except Exception as e:
        print(f"Error: {str(e)}")
        return []