#!/usr/bin/env python3

import unittest

from preprocessing import read_object_classes


class TestPreprocessing(unittest.TestCase):
    def test_read_object_classes(self):
        map_filename = 'test_category_maps/stanford_bground_categories.txt'
        category_colors, category_names = read_object_classes(map_filename)
        self.assertEqual(category_colors[0], (int(0.3700 * 255), int(0.7300 * 255), int(0.9900 * 255)))
        self.assertEqual(category_colors[1], (int(0.1500 * 255), int(0.3100 * 255), int(0.0700 * 255)))
        self.assertEqual(category_colors[2], (int(0.2600 * 255), int(0.2600 * 255), int(0.2600 * 255)))
        self.assertEqual(category_colors[3], (int(0.4200 * 255), int(0.6600 * 255), int(0.3100 * 255)))
        self.assertEqual(category_colors[4], (int(0.0700 * 255), int(0.3300 * 255), int(0.8000 * 255)))
        self.assertEqual(category_colors[5], (int(0.8800 * 255), int(0.4000 * 255), int(0.4000 * 255)))
        self.assertEqual(category_colors[6], (int(0.8100 * 255), int(0.8900 * 255), int(0.9500 * 255)))
        self.assertEqual(category_colors[7], (int(0.9500 * 255), int(0.7600 * 255), int(0.2000 * 255)))

        category_names_correct = ["sky", "tree/bush", "road/path", "grass", "water", "building", "mountain",
                                  "foreground_object"]
        self.assertListEqual(category_names, category_names_correct)

    def image_to_np_array(self):
        pass

    def np_array_to_image(self):
        pass

    def labels_to_np_array(self):
        pass

    def text_labels_to_np_array(self):
        pass

    def save_labels_array(self):
        pass

    def get_patch(self):
        pass

    def interleave_images(self):
        pass

    def get_sorted_files_in_folder(self):
        pass

    def from_games_dataset(self):
        pass

    def stanford_bgrounds_dataset(self):
        pass
