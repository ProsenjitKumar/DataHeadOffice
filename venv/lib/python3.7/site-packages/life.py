"""
Game of Life in Python3
"""

import subprocess
import functools
import argparse
import random
import time
import re

version = "1.0.0"


def print_grid(grid, grid_width):
    """
    Print grid.
    """

    i = 0
    while i < len(grid):
        print("".join(grid[i:i+grid_width]))
        i += grid_width


def tick(grid, map_rule):
    """
    Tick.
    """

    return list(map(map_rule, enumerate(grid)))


def rule(grid, grid_width, alive, dead, cell):
    """
    Define rule of the game.
    """

    index = cell[0]
    itself = cell[1]
    neighbors = [
        grid[index - grid_width - 1],
        grid[index - grid_width],
        grid[index - grid_width + 1],
        grid[index - 1],
        grid[(index + 1) % len(grid)],
        grid[(index + grid_width - 1) % len(grid)],
        grid[(index + grid_width) % len(grid)],
        grid[(index + grid_width + 1) % len(grid)]
    ]
    living_neighbors = list(filter(lambda n: n == alive, neighbors))
    if len(living_neighbors) < 2:  # under-population
        return dead
    elif len(living_neighbors) > 3:  # over-population
        return dead
    elif len(living_neighbors) == 3:  # reproduction
        return alive
    else:
        return itself


def parse_arguments():
    """
    Parse arguments.
    """

    d = {
        "prog": "con",
        "description": "Game of Life",
        "epilog": "Coded by nsgonultas, licensed under CC BY-NC 4.0"
                  "\nhttps://github.com/nsgonultas/life"
    }
    parser = argparse.ArgumentParser(**d)
    parser.add_argument("-f", "--file", help="Set input file")
    parser.add_argument("-r", "--rows", metavar="NUM", type=int, default=10,
                        help="Set row number")
    parser.add_argument("-c", "--cols", metavar="NUM", type=int, default=10,
                        help="Set column number")
    parser.add_argument("-a", "--alive", metavar="CHR", default="#",
                        help="Set the character that represents alive cells")
    parser.add_argument("-d", "--dead", metavar="CHR", default=".",
                        help="Set the character that represents dead cells")
    parser.add_argument("-s", action="count", dest="speed", help="Set the"
                        " game speed e.g. -sss: 3 generations per second")
    parser.add_argument("-l", "--limit", metavar="NUM", type=int,
                        help="Limits generation")
    parser.add_argument("-e", "--enumerate", action="store_true",
                        help="Enumerates generations")
    parser.add_argument("-n", "--normalize", action="store_true",
                        help="Normalizes output for redirections")
    parser.add_argument("-v", "--version", action="version",
                        version="%(prog)s " + version)

    ns = parser.parse_args()
    return ns


def main():
    args = parse_arguments()
    alive = args.alive
    dead = args.dead
    redirection_mode = args.normalize

    # create grid
    if args.file is not None:
        with open(args.file) as f:
            content = f.read()
            lines = content.split("\n")[:-1]
            grid = []
            for line in lines:
                grid += list(line)
            grid_width = len(lines[0])
            grid_height = len(lines)
            content = content.replace("\n", "")
            pattern = re.compile("^[" + alive + dead + "]*$")
            if pattern.match(content) is None:
                print("ERROR: Input file contains unrecognized characters")
                exit(1)
    else:
        grid = []
        grid_width = args.cols
        grid_height = args.rows
        for i in range(grid_width * grid_height):
            if random.random() < .2:
                grid.append(alive)
            else:
                grid.append(dead)

    # set speed
    if args.speed is not None:
        delay = 1 / args.speed
    else:
        delay = (.25)  # seconds

    # limit generation number
    if args.limit is not None:
        limit = args.limit
        limited = True
    else:
        limited = False

    # i think i could use a string to represent gen_number
    # but for now i'll leave it
    gen_number = 0

    while True:
        if not redirection_mode:
            subprocess.call(["clear"])
        if args.enumerate:
            print("Generation number:", gen_number)
        print_grid(grid, grid_width)
        time.sleep(delay)
        maprule = functools.partial(rule, grid, grid_width, alive, dead)
        grid = tick(grid, maprule)
        gen_number += 1
        if limited and gen_number == limit:
            break


if __name__ == "__main__":
    main()
