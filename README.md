# Toy-Robot-Simulator


## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Folder Structure](#folder-structure)
- [Configuration](#configuration)
- [Commands](#commands)
- [Tests](#tests)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The application is a simulation of a toy robot moving on a square tabletop, of dimensions 5 units x 5 units. There are no other obstructions on the table surface. The robot is free to roam around the surface of the table, but must be prevented from falling to destruction. Any movement that would result in the robot falling from the table must be prevented, however further valid movement commands must still be allowed.

## Features

- **Placement**: Place the robot on the table with specified coordinates and facing direction.
- **Movement**: Move the robot one unit in the direction it is facing.
- **Rotation**: Rotate the robot 90 degrees left or right without changing its position.
- **Reporting**: Output the current coordinates and facing direction of the robot.
- **Error Handling**: Invalid commands or moves that would cause the robot to fall off the table are ignored.

## Getting Started

### Prerequisites

Before you begin, ensure you have met the following requirements:

- [Python](https://www.python.org/downloads/): Ensure Python is installed on your system. You can download Python from the official website.

### Installation
   
1. Clone the repository:
   
   ```bash
   git clone git@github.com:prarthana1998/Toy-Robot-Simulator.git

2. Navigate to the project src directory
   ```bash
   cd Toy-Robot-Simulator/src

3. Run 
   ```python
   python main.py 

### Folder Structure

- Toy-Robot-Simulator
  - README.md
  - src
    - robot.py
    - table.py
    - main.py
    - utils.py
    - commands.py
  - tests
    - test_robot.py
    - test_table.py
    - test_rotation.py
  - config
    - config.json
  - input.txt

### Configuration

The Toy Robot Simulator uses a configuration file `config.json` located in the `config` folder. You can specify the commands file path in this configuration:
    ```json
     
    {
    "commands_file": "../input.txt"
    }

### Commands
The simulator accepts the following commands:

- **PLACE X,Y,FACING:** Place the robot on the table at position X,Y and facing NORTH, SOUTH, EAST, or WEST.
- **MOVE:** Move the robot one unit in the direction it is facing.
- **LEFT:** Rotate the robot 90 degrees to the left.
- **RIGHT:** Rotate the robot 90 degrees to the right.
- **REPORT:** Output the current coordinates and facing direction of the robot.

### Tests

To run the unit tests for the Toy Robot Simulator, use the following command:
    
      
      PYTHONPATH=src python -m unittest discover -s tests -p 'test_*.py'
   
### Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or a pull request on GitHub. <br>

### License
This project is licensed under the MIT License.





