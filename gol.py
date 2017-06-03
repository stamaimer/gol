# -*- coding: utf-8 -*-

import os
import time
import numpy as np


def get_around_8_index(row, col):

    indices = [(row-1, col-1), (row-1, col), (row-1, col+1),
               (row, col-1), (row, col+1),
               (row+1, col-1), (row+1, col), (row+1, col+1)]

    invalid_indices = [item for item in indices if item[0] == -1 or item[0] == world_size or
                                                   item[1] == -1 or item[1] == world_size]

    valid_indices = [item for item in indices if item not in invalid_indices]

    return valid_indices


def game_of_life(world_size, live_ratio, count):

    world = np.random.choice([0, 1],
                             size=world_size * world_size,
                             p=[1 - live_ratio, live_ratio]).reshape(world_size, world_size)
    while 1:

        print world

        new_world = np.copy(world)

        for row in xrange(world_size):

            for col in xrange(world_size):

                indices = get_around_8_index(row, col)

                cell = [world[r][c] for r, c in indices]

                live_cell_count = sum(cell)

                if world[row][col]:  # live

                    if live_cell_count < 2 or live_cell_count > 3:

                        new_world[row][col] = 0

                else:  # dead

                    if live_cell_count == 3:

                        new_world[row][col] = 1

        world = new_world

        time.sleep(1 / count)

        os.system("clear")


if __name__ == "__main__":

    world_size = int(raw_input("Please input the size of the world:"))

    live_ratio = float(raw_input("Please input the cell live ratio in the world([0, 1]):"))

    count = int(raw_input("Please input the generations you want in each second:"))

    game_of_life(world_size, live_ratio, count)
