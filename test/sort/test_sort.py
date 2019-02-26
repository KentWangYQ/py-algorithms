# -*- coding: utf-8 -*-

import unittest
import random
import copy

from source.sort import sort


class SortTest(unittest.TestCase):
    def setUp(self):
        self.a = [3, 2, -20, 309, -987, 2, 487, -20, 90, -5, 0, 98]
        self.b = copy.deepcopy(self.a)

    def test_insertion_sort(self):
        sort.insertion_sort(self.b)
        list.sort(self.a)
        self.assertEqual(self.a, self.b, 'The list is NOT sorted after insertion sort!')

    def test_insertion_sort_reverse(self):
        sort.insertion_sort(a=self.b, reverse=True)
        list.sort(self.a, reverse=True)
        self.assertEqual(self.a, self.b, 'The list is NOT sorted after insertion sort reverse!')

    def test_merge_sort(self):
        sort.merge_sort(self.b)
        list.sort(self.a)
        self.assertEqual(self.a, self.b, 'The list is NOT sorted after merge sort!')

    def test_merge_sort_reverse(self):
        sort.merge_sort(a=self.b, reverse=True)
        list.sort(self.a, reverse=True)
        self.assertEqual(self.a, self.b, 'The list is NOT sorted after merge sort reverse!')

    def test_heap_sort(self):
        sort.heap_sort(self.b)
        list.sort(self.a)
        self.assertEqual(self.a, self.b, 'The list is NOT sorted after heap sort!')

    def test_heap_sort_reverse(self):
        sort.heap_sort(self.b, reverse=True)
        list.sort(self.a, reverse=True)
        self.assertEqual(self.a, self.b, 'The list is NOT sorted after heap sort reverse!')

    def test_quick_sort(self):
        sort.quick_sort(self.b)
        list.sort(self.a)
        self.assertEqual(self.a, self.b, 'The list is NOT sorted after quick sort!')

    def test_quick_sort_reverse(self):
        sort.quick_sort(self.b, reverse=True)
        list.sort(self.a, reverse=True)
        self.assertEqual(self.a, self.b, 'The list is NOT sorted after quick sort reverse!')

    def test_quick_sort_rd(self):
        sort.quick_sort(self.b, randomized_partition=True)
        list.sort(self.a)
        self.assertEqual(self.a, self.b, 'The list is NOT sorted after quick sort!')

    def test_quick_sort_reverse_rd(self):
        sort.quick_sort(self.b, reverse=True, randomized_partition=True)
        list.sort(self.a, reverse=True)
        self.assertEqual(self.a, self.b, 'The list is NOT sorted after quick sort reverse!')

    def test_sort_random_list(self):
        t = 1000
        a = [random.randint(t * -1, t) for _ in range(t)]

        insertion_sort = copy.deepcopy(a)
        sort.insertion_sort(insertion_sort)

        a_merge_sort = copy.deepcopy(a)
        sort.merge_sort(a_merge_sort)

        a_heap_sort = copy.deepcopy(a)
        sort.heap_sort(a_heap_sort)

        a_quick_sort = copy.deepcopy(a)
        sort.quick_sort(a_quick_sort)

        list.sort(a)

        self.assertEqual(a, insertion_sort, 'The list is NOT sorted after insertion sort!')
        self.assertEqual(a, a_merge_sort, 'The list is NOT sorted after merge sort!')
        self.assertEqual(a, a_heap_sort, 'The list is NOT sorted after heap sort!')
        self.assertEqual(a, a_quick_sort, 'The list is NOT sorted after quick sort!')

    def test_sort_random_list_reverse(self):
        t = 1000
        a = [random.randint(t * -1, t) for _ in range(t)]

        a_insertion_sort = copy.deepcopy(a)
        sort.insertion_sort(a_insertion_sort, reverse=True)

        a_merge_sort = copy.deepcopy(a)
        sort.merge_sort(a_merge_sort, reverse=True)

        a_heap_sort = copy.deepcopy(a)
        sort.heap_sort(a_heap_sort, reverse=True)

        a_quick_sort = copy.deepcopy(a)
        sort.quick_sort(a_quick_sort, reverse=True)

        list.sort(a, reverse=True)

        self.assertEqual(a, a_insertion_sort, 'The list is NOT sorted after insertion sort reverse!')
        self.assertEqual(a, a_merge_sort, 'The list is NOT sorted after merge sort reverse!')
        self.assertEqual(a, a_heap_sort, 'The list is NOT sorted after heap sort reverse!')
        self.assertEqual(a, a_quick_sort, 'The list is NOT sorted after quick sort reverse!')

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
