# -*- coding: utf-8 -*-

import unittest
import copy

from source.tree.heap import MaxHeap, MinHeap


class MaxHeapTest(unittest.TestCase):
    def setUp(self):
        """
        Max heap binary tree
                 ____487_____
                /            \
             _309_           98
            /     \         /  \
          90      0        3   -20
         /  \    / \      /
       -20  2  -5 -987   2
        :return:
        """
        self.a = [3, 2, -20, 309, -987, 2, 487, -20, 90, -5, 0, 98]
        self.max_heap = MaxHeap(copy.deepcopy(self.a))
        self.assertTrue(self.max_heap.heap_check(), 'The heap is NOT a max heap!')

    def test_heap_check(self):
        max_heap = MaxHeap()
        max_heap.A = [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]
        max_heap.heap_size = len(max_heap.A)
        self.assertTrue(max_heap.heap_check(), 'The list is a max heap, but return False!')

        max_heap.A = [16, 14, 9, 8, 7, 10, 3, 2, 4, 1]
        max_heap.heap_size = len(max_heap.A)
        self.assertFalse(max_heap.heap_check(), 'The list is NOT a max heap, but return True!')

    def test_heap_sort(self):
        self.max_heap.heap_sort()
        list.sort(self.a)
        self.assertEqual(self.a, self.max_heap.A, 'The list is NOT sorted after max heap sort!')

    def test_maximum(self):
        self.assertEqual(max(self.a), self.max_heap.maximum(), 'The result is NOT the maximum of heap!')

    def test_extract_max(self):
        max_key = self.max_heap.extract_max()
        self.assertEqual(max(self.a), max_key, 'The key extract for max_heap is NOT the max key!')
        self.assertTrue(self.max_heap.heap_check(), 'The heap is NOT a max heap after extract key!')

    def test_increase_key(self):
        self.max_heap.increase_key(4, 100)
        self.assertEqual(4, self.max_heap.A.index(100), 'The new key is NOT at the right place after increase key!')
        self.assertTrue(self.max_heap.heap_check(), 'The heap is NOT a max heap after increase key!')

    def test_insert(self):
        keys = [0, 10, 999, -999, 100, 2]
        for key in keys:
            self.max_heap.insert(key)
        self.assertTrue(self.max_heap.heap_check(), 'The heap is NOT a max heap after insert keys!')


class MinHeapTest(unittest.TestCase):
    def setUp(self):
        """
        Min heap binary tree
                    __-987____
                   /          \
                _-20_        -20
               /     \       /  \
              3      -5     2  487
            / \     / \    /
        309   90   2  0   98
        :return:
        """
        self.a = [3, 2, -20, 309, -987, 2, 487, -20, 90, -5, 0, 98]
        self.min_heap = MinHeap(copy.deepcopy(self.a))
        self.assertTrue(self.min_heap.heap_check(), 'The heap is NOT a min heap!')

    def test_heap_check(self):
        min_heap = MinHeap()
        min_heap.A = [1, 2, 3, 4, 7, 8, 9, 10, 14, 16]
        min_heap.heap_size = len(min_heap.A)
        self.assertTrue(min_heap.heap_check(), 'The list is a min heap, but return False!')

        min_heap.A = [1, 7, 3, 4, 2, 8, 9, 10, 14, 16]
        min_heap.heap_size = len(min_heap.A)
        self.assertFalse(min_heap.heap_check(), 'The list is NOT a min heap, but return True!')

    def test_heap_sort(self):
        self.min_heap.heap_sort()
        list.sort(self.a, reverse=True)
        self.assertEqual(self.a, self.min_heap.A, 'The list is NOT sorted after min heap sort!')

    def test_minimum(self):
        self.assertEqual(min(self.a), self.min_heap.minimum(), 'The result is NOT the minimum of heap!')

    def test_extract_min(self):
        _min = self.min_heap.extract_min()
        self.assertEqual(min(self.a), _min, 'The key extract from min_heap if NOT the min key!')
        self.assertTrue(self.min_heap.heap_check(), 'The heap is NOT a min heap after extract min!')

    def test_decrease_key(self):
        self.min_heap.decrease_key(8, -30)
        self.assertEqual(1, self.min_heap.A.index(-30), 'The new key is NOT at the right place after decrease key!')
        self.assertTrue(self.min_heap.heap_check(), 'The heap is NOT a min heap after decrease key!')

    def test_insert(self):
        keys = [0, 10, 999, -999, 100, 2]
        for key in keys:
            self.min_heap.insert(key)
        self.assertTrue(self.min_heap.heap_check(), 'The heap is NOT a min heap after insert keys!')
