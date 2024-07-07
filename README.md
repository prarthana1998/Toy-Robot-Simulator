# Toy-Robot-Simulator


## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
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

- Python 3.x
- Git (optional)

### Installation

1. Clone the repository: to your local machine
   
```bash
  git clone git@github.com:prarthana1998/Toy-Robot-Simulator.git

2. Navigate to the project src directory
 ```bash
  cd /Toy-Robot-Simulator/src

3. Run ```bash python main.py 

4. 

