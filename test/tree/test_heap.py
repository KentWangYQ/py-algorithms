# -*- coding: utf-8 -*-

import unittest

from source.tree.heap import Heap, MaxHeap, MinHeap


class MaxHeapTest(unittest.TestCase):
    def test_heap_sort(self):
        a = [3, 2, -20, 309, -987, 2, 487, -20, 90, -5, 0, 98]
        max_heap = MaxHeap(a=a)
        max_heap.heap_sort()
        list.sort(a)
        self.assertEqual(a, max_heap.A, 'The list is NOT sorted after max heap sort!')


class MinHeapTest(unittest.TestCase):
    def test_heap_sort(self):
        a = [3, 2, -20, 309, -987, 2, 487, -20, 90, -5, 0, 98]
        min_heap = MinHeap(a=a)
        min_heap.heap_sort()
        list.sort(a, reverse=True)
        self.assertEqual(a, min_heap.A, 'The list is NOT sorted after min heap sort!')
