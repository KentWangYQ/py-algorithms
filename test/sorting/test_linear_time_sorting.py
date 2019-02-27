# -*- coding: utf-8 -*-

import unittest
import copy

from source.sorting import linear_time_sorting


class LinearTimeSortingTest(unittest.TestCase):
    def setUp(self):
        self.a = [100, 62, 5426, 34356, 503, 46, 0, 313569, 187, 85, 6, 5400]
        self.max = max(self.a)
        self.k = len(str(self.max))

    def test_counting_sort(self):
        counting_sort_result = linear_time_sorting.counting_sort(self.a, self.max)
        list.sort(self.a)
        self.assertEqual(self.a, counting_sort_result, 'The list is NOT sorted after counting sort!')

    def test_counting_sort_reverse(self):
        counting_sort_reverse_result = linear_time_sorting.counting_sort(self.a, self.max, reverse=True)
        list.sort(self.a, reverse=True)
        self.assertEqual(self.a, counting_sort_reverse_result, 'The list is NOT sorted after counting sort reverse!')

    def test_radix_sort(self):
        radix_sort_result = linear_time_sorting.radix_sort(self.a, self.k)
        list.sort(self.a)
        self.assertEqual(self.a, radix_sort_result, 'The list is NOT sorted after radix sort!')

    def test_radix_reverse_sort(self):
        radix_sort_reverse_result = linear_time_sorting.radix_sort(self.a, self.k, reverse=True)
        list.sort(self.a, reverse=True)
        self.assertEqual(self.a, radix_sort_reverse_result, 'The list is NOT sorted after radix sort reverse!')
