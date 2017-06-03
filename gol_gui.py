# -*- coding: utf-8 -*-

import time
import numpy as np
from Tkinter import *


def draw_a_rect(x, y, status, can):

    if status:

        can.create_rectangle(x, y, x + 5, y + 5, fill="black")

    else:

        can.create_rectangle(x, y, x + 5, y + 5)


def get_around_index(row, col, world_size):

    indices = [(row - 1, col - 1), (row - 1, col), (row - 1, col + 1),
               (row, col - 1), (row, col + 1),
               (row + 1, col - 1), (row + 1, col), (row + 1, col + 1)]

    invalid_indices = [item for item in indices if item[0] == -1 or item[0] == world_size or
                                                   item[1] == -1 or item[1] == world_size]

    valid_indices = [item for item in indices if item not in invalid_indices]

    return valid_indices


def print_world(world, world_size, can):

    for row in xrange(world_size):

        for col in xrange(world_size):

            draw_a_rect(row * 5, col * 5, world[row][col], can)


def game_of_life(world, world_size):

    new_world = np.copy(world)

    for row in xrange(world_size):

        for col in xrange(world_size):

            indices = get_around_index(row, col, world_size)

            cell = [world[r][c] for r, c in indices]

            live_cell_count = sum(cell)

            if world[row][col]:  # live

                if live_cell_count < 2 or live_cell_count > 3:

                    new_world[row][col] = 0

            else:  # dead

                if live_cell_count == 3:

                    new_world[row][col] = 1

    return new_world

if __name__ == "__main__":

    root = Tk()

    top_frame = Frame(root)
    top_frame.pack(side="top")

    bot_frame = Frame(root)
    bot_frame.pack(side="bottom")

    world_size_entry = Entry(top_frame)
    world_size_entry.insert(0, "size of the world")
    world_size_entry.pack(side="left")

    live_ratio_entry = Entry(top_frame)
    live_ratio_entry.insert(0, "ration of the live")
    live_ratio_entry.pack(side="left")

    count_entry = Entry(top_frame)
    count_entry.insert(0, "generation count")
    count_entry.pack(side="left")

    def callback():

        world_size = int(world_size_entry.get())
        live_ratio = float(live_ratio_entry.get())
        count = int(count_entry.get())

        can = Canvas(bot_frame)
        can.place(relx=.5, rely=.5, anchor=CENTER)
        can.pack(expand=1)

        world = np.random.choice([0, 1],
                                 size=world_size * world_size,
                                 p=[1 - live_ratio, live_ratio]).reshape(world_size, world_size)

        while 1:

            world = game_of_life(world, world_size)

            can.delete("all")

            print_world(world, world_size, can)

            root.update_idletasks()

            root.update()

            time.sleep(1/count)

    start_button = Button(top_frame, text="Start", command=callback)

    start_button.pack(side="left")

    root.mainloop()
