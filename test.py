# -*- coding: utf-8 -*-

import unittest

import numpy as np

from gol_gui import get_around_index, game_of_life


class TestStringMethods(unittest.TestCase):

    def test_game_of_life(self):

        old_world = np.array([[1, 0, 1], [0, 1, 0], [1, 0, 1]])

        expected_new_world = np.array([[0, 1, 0], [1, 0, 1], [0, 1, 0]])

        self.assertListEqual(expected_new_world.tolist(), game_of_life(old_world, 3).tolist())

        self.assertListEqual(expected_new_world.tolist(), game_of_life(expected_new_world, 3).tolist())

    def test_get_around_index_about_cornor(self):

        expected_indices = [(0, 1), (1, 0), (1, 1)]

        self.assertListEqual(expected_indices, get_around_index(0, 0, 3))

    def test_get_around_index_about_side(self):

        expected_indices = [(0, 0), (0, 2), (1, 0), (1, 1), (1, 2)]

        self.assertListEqual(expected_indices, get_around_index(0, 1, 3))

    def test_get_around_index_about_center(self):

        expected_indices = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1), (2, 2)]

        self.assertListEqual(expected_indices, get_around_index(1, 1, 3))


if __name__ == '__main__':
    unittest.main()