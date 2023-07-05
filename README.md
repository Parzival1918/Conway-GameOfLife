# Game of Life

![](docs/game-of-life-vid-standalone.gif)

Conway's Game of life in python

* This program has been coded to test how the **curses** python module works.

Run and see the Game play updating every 0.1 seconds. Press <**q**> to exit, or <**CTRL+C**> to kill the program. 

In edit mode, press <**SPACE**> to toggle the cell state. Press <**q**> to start resume the game.

## Installation

* `pipx install game-of-life-uc`. You must install `pipx` first if you don't have it already.
* Run with `game-of-life`

### Dependencies

* curses
* time
* random
* copy
* argparse

## To-Do

* Add a How-To window (curses.newwin())