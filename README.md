# Game of Life

![](docs/game-of-life-vid-standalone.gif)

Conway's Game of life in python

* This program has been coded to test how the **curses** python module works.

Run and see the Game play updating every 0.1 seconds. Press <**q**> to exit, or <**CTRL+C**> to kill the program. 

In edit mode, press <**SPACE**> to toggle the cell state. Press <**q**> to start resume the game.

## Installation

This was developed using Python 3.11.4.

1. Clone the repository `git clone https://github.com/Parzival1918/Conway-GameOfLife.git`
2. Change directory to the repository `cd Conway-GameOfLife/code`
3. Run the program `python3 game_of_life.py`

If you want to run the code from anywhere, you can add the code directory to your PATH variable and set it as an executable with the command `chmod +x game-of-life.py`. First you will need to change the first line of the file to `#!/usr/bin/python3` or something else depending on your system, basically the path to your python3 installation in your system. After that you can run the program from anywhere in your system by typing `game-of-life.py` in your terminal.

### Dependencies

* curses
* time
* random
* copy
* argparse

## To-Do

* Add a How-To window (curses.newwin())