#!/opt/homebrew/bin/python3

#Conway's game of life

import curses
from curses import wrapper
import random
import time

#Cell class
class Cell:
    def __init__(self, alive: bool = False):
        self.alive = alive

    #Toggle cell state
    def toggle(self):
        self.alive = not self.alive

    #Set cell state depending on number of neighbors
    def set_state(self, neighbors: int):
        if self.alive:
            if neighbors < 2 or neighbors > 3:
                self.alive = False
        else:
            if neighbors == 3:
                self.alive = True

#Grid class
class Grid:
    def __init__(self, height: int, width: int):
        self.height = height
        self.width = width
        self.cells = [[Cell() for i in range(width)] for j in range(height)]
        self.generation = 0

    #Toggle cell state
    def toggle(self, y: int, x: int):
        self.cells[y][x].toggle()

    #Get number of neighbors
    def get_neighbors(self, y: int, x: int):
        neighbors = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0: continue
                if y + i < 0 or y + i >= self.height: continue
                if x + j < 0 or x + j >= self.width: continue
                if self.cells[y + i][x + j].alive: neighbors += 1
        return neighbors

    #Run one iteration of the game
    def run(self):
        for y in range(self.height):
            for x in range(self.width):
                neighbors = self.get_neighbors(y, x)
                self.cells[y][x].set_state(neighbors)

        self.generation += 1

    #Assign random state to cells
    def randomize(self):
        self.generation = 0

        for y in range(self.height):
            for x in range(self.width):
                self.cells[y][x].alive = random.choice([True, False])

def main(stdscr):
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_WHITE)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)
    DEAD = curses.color_pair(1)
    ALIVE = curses.color_pair(2)
    TEXT = curses.color_pair(3)

    #Do not wait for keypress
    stdscr.nodelay(True)
    #Disable cursor
    curses.curs_set(0)

    #Get screen size
    height, width = stdscr.getmaxyx()

    #Create grid
    grid = Grid(height-2, width-2) #Leave space for border

    #Randomize grid
    grid.randomize()

    #Run game
    while True:
        stdscr.clear()

        #Add window border
        stdscr.border()

        #Print text
        stdscr.addstr(0, 1, "Press q to quit, r to randomize", TEXT)
        stdscr.addstr(0, width-20, "Generation: " + str(grid.generation), TEXT)

        try:
            key_pressed = stdscr.getch()
        except:
            key_pressed = None
        
        #Exit if q is pressed, if r is pressed randomize grid
        if key_pressed == 113:
            break
        elif key_pressed == 114:
            grid.randomize()

        #Print grid
        for y in range(grid.height):
            for x in range(grid.width):
                if grid.cells[y][x].alive:
                    pass
                    stdscr.addstr(1+y, 1+x, " ", ALIVE)
                else:
                    pass
                    stdscr.addstr(1+y, 1+x, " ", DEAD)

        stdscr.refresh()

        #Run one iteration
        grid.run()

        #Wait for keypress
        time.sleep(0.1)

    #Exit

if __name__ == "__main__":
    wrapper(main)