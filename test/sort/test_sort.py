# -*- coding: utf-8 -*-

import unittest
import random
import copy

from source.sort import sort


class SortTest(unittest.TestCase):
    def test_insertion_sort(self):
        a = [3, 2, -20, 309, -987, 2, 487, -20, 90, -5, 0, 98]
        insertion_sort_result = sort.insertion_sort(copy.deepcopy(a))
        list.sort(a)
        self.assertEqual(a, insertion_sort_result, 'The list is NOT sorted after insertion sort!')

    def test_insertion_sort_reverse(self):
        a = [3, 2, -20, 309, -987, 2, 487, -20, 90, -5, 0, 98]
        insertion_sort_result = sort.insertion_sort(copy.deepcopy(a), reverse=True)
        list.sort(a, reverse=True)
        self.assertEqual(a, insertion_sort_result, 'The list is NOT sorted after insertion sort reverse!')

    def test_merge_sort(self):
        a = [3, 2, -20, 309, -987, 2, 487, -20, 90, -5, 0, 98]
        merge_sort_result = copy.deepcopy(a)
        sort.merge_sort(merge_sort_result, 0, len(a) - 1)
        list.sort(a)
        self.assertEqual(a, merge_sort_result, 'The list is NOT sorted after merge sort!')

    def test_merge_sort_reverse(self):
        a = [3, 2, -20, 309, -987, 2, 487, -20, 90, -5, 0, 98]
        merge_sort_result = copy.deepcopy(a)
        sort.merge_sort(merge_sort_result, 0, len(merge_sort_result) - 1, reverse=True)
        list.sort(a, reverse=True)
        self.assertEqual(a, merge_sort_result, 'The list is NOT sorted after merge sort reverse!')

    def test_sort_random_list(self):
        t = 1000
        a = [random.randint(t * -1, t) for _ in range(t)]

        insertion_sort_result = sort.insertion_sort(copy.deepcopy(a))

        merge_sort_result = copy.deepcopy(a)
        sort.merge_sort(merge_sort_result, 0, len(merge_sort_result) - 1)

        list.sort(a)

        self.assertEqual(a, insertion_sort_result, 'The list is NOT sorted after insertion sort!')
        self.assertEqual(a, merge_sort_result, 'The list is NOT sorted after merge sort!')

    def test_sort_random_list_reverse(self):
        t = 1000
        a = [random.randint(t * -1, t) for _ in range(t)]

        insertion_sort_result = sort.insertion_sort(copy.deepcopy(a), reverse=True)

        merge_sort_result = copy.deepcopy(a)
        sort.merge_sort(merge_sort_result, 0, len(merge_sort_result) - 1, reverse=True)

        list.sort(a, reverse=True)

        self.assertEqual(a, insertion_sort_result, 'The list is NOT sorted after insertion sort reverse!')
        self.assertEqual(a, merge_sort_result, 'The list is NOT sorted after merge sort reverse!')

    def test_merge(self):
        p, q, r = 1, 5, 10
        a = [3, 2, -20, 309, -987, 2, 487, -20, 90, -5, 0, 98]
        lv = a[p:q + 1]
        rv = a[q + 1:r + 1]
        list.sort(lv)
        list.sort(rv)
        a[p:q + 1] = lv
        a[q + 1:r + 1] = rv

        actual = copy.deepcopy(a)
        sort._merge(actual, p, q, r)
        expect = a[p:r + 1]
        list.sort(expect)

        self.assertEqual(expect, actual[p:r + 1], 'The %d to %d items in list is NOT sorted after merge!' % (p, r + 1))

    def test_merge_reverse(self):
        p, q, r = 1, 5, 10
        a = [3, 2, -20, 309, -987, 2, 487, -20, 90, -5, 0, 98]
        lv = a[p:q + 1]
        rv = a[q + 1:r + 1]
        list.sort(lv, reverse=True)
        list.sort(rv, reverse=True)
        a[p:q + 1] = lv
        a[q + 1:r + 1] = rv

        actual = copy.deepcopy(a)
        sort._merge(actual, p, q, r, reverse=True)
        expect = a[p:r + 1]
        list.sort(expect, reverse=True)

        self.assertEqual(expect, actual[p:r + 1],
                         'The %d to %d items in list is NOT sorted after merge reverse!' % (p, r + 1))
