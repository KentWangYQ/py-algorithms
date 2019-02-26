# -*- coding: utf-8 -*-

import unittest

from source.sorting import linear_time_sorting


class LinearTimeSortingTest(unittest.TestCase):
    def setUp(self):
        self.k = 100
        self.a = [10, 6, 54, 36, 5, 46, 0, 3, 7, 85, 6, 54]

    def test_counting_sort(self):
        counting_sort_result = linear_time_sorting.counting_sort(self.a, self.k)
        list.sort(self.a)
        self.assertEqual(self.a, counting_sort_result, 'The list is NOT sorted after counting sort!')

    def test_counting_sort_reverse(self):
        counting_sort_reverse_result = linear_time_sorting.counting_sort(self.a, self.k, reverse=True)
        list.sort(self.a, reverse=True)
        self.assertEqual(self.a, counting_sort_reverse_result, 'The list is NOT sorted after counting sort reverse!')
