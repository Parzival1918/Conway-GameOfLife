#!/opt/homebrew/bin/python3

#Parse the command line arguments

import argparse
import game_of_life

parser = argparse.ArgumentParser()

parser.add_argument("-w", "--wrap", help="Wrap around the edges of the grid", action="store_true")
parser.add_argument("-s", "--speed", type=float, default=0.1, help="Time between iterations in seconds, default [0.1]")

game_of_life.call_game_of_life(parser.parse_args())
