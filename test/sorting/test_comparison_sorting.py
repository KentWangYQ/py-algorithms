# -*- coding: utf-8 -*-

import unittest
import random
import copy

from source.sorting import comparison_sorting
from source.sorting.comparison_sorting import SLNode


class ComparisionSortTest(unittest.TestCase):
    def setUp(self):
        self.a = [3, 2, -20, 309, -987, 2, 487, -20, 90, -5, 0, 98]
        self.b = copy.deepcopy(self.a)

    # region INSERTION SORT
    # 直接插入排序测试
    def test_straight_insertion_sort(self):
        """
        直接插入排序测试
        :return:
        """
        comparison_sorting.straight_insertion_sort(self.b)
        list.sort(self.a)
        self.assertEqual(self.a, self.b, 'The list is NOT sorted after straight insertion sort!')

    # 直接插入倒序排序测试
    def test_straight_insertion_sort_reverse(self):
        """
        直接插入倒序排序测试
        :return:
        """
        comparison_sorting.straight_insertion_sort(a=self.b, reverse=True)
        list.sort(self.a, reverse=True)
        self.assertEqual(self.a, self.b, 'The list is NOT sorted after straight insertion sort reverse!')

    # 折半插入排序测试
    def test_binary_insertion_sort(self):
        """
        折半插入排序测试
        :return:
        """
        comparison_sorting.binary_insertion_sort(self.b)
        list.sort(self.a)
        self.assertEqual(self.a, self.b, 'The list is NOT sorted after binary insertion sort!')

    # 折半插入倒序排序测试
    def test_binary_insertion_sort_reverse(self):
        """
        折半插入倒序排序测试
        :return:
        """
        comparison_sorting.binary_insertion_sort(self.b, True)
        list.sort(self.a, reverse=True)
        self.assertEqual(self.a, self.b, 'The list is NOT sorted after binary insertion sort reverse!')

    # 2路插入排序测试
    def test_two_way_insertion_sort(self):
        """
        2路插入排序测试
        :return:
        """
        comparison_sorting.two_way_insertion_sort(self.b)
        list.sort(self.a)
        self.assertEqual(self.a, self.b, 'The list is NOT sorted after two way insertion sort!')

    # 2路插入倒序排序测试
    def test_two_way_insertion_sort_reverse(self):
        """
        2路插入倒序排序测试
        :return:
        """
        comparison_sorting.two_way_insertion_sort(self.b, True)
        list.sort(self.a, reverse=True)
        self.assertEqual(self.a, self.b, 'The list is NOT sorted after two way insertion sort reverse!')

    # 表插入排序测试
    def test_list_insertion_sort(self):
        """
        表插入排序测试
        :return:
        """
        comparison_sorting.list_insertion_sort(self.b)
        list.sort(self.a)
        self.assertEqual(self.a, self.b, 'The list is NOT sorted after link list insertion sort!')

    # 表插入倒序排序测试
    def test_list_insertion_sort_reverse(self):
        """
        表插入倒序排序测试
        :return:
        """
        comparison_sorting.list_insertion_sort(self.b, True)
        list.sort(self.a, reverse=True)
        self.assertEqual(self.a, self.b, 'The list is NOT sorted after link list insertion sort reverse!')

    # 重排链表测试
    def test_arrange(self):
        """
        重排链表测试
        :return:
        """
        _keys, _next = [float('inf'), 49, 38, 76, 13, 27], [4, 3, 1, 0, 5, 2]
        sl = [SLNode(k, _next[i]) for i, k in enumerate(_keys)]
        comparison_sorting._arrange(sl)
        expect = _keys[1:]
        list.sort(expect)

        actual = [sln.rc for sln in sl[1:]]

        self.assertEqual(expect, actual, 'The link list is NOT sorted after _arrange!')

    # endregion

    def test_merge_sort(self):
        comparison_sorting.merge_sort(self.b)
        list.sort(self.a)
        self.assertEqual(self.a, self.b, 'The list is NOT sorted after merge sort!')

    def test_merge_sort_reverse(self):
        comparison_sorting.merge_sort(a=self.b, reverse=True)
        list.sort(self.a, reverse=True)
        self.assertEqual(self.a, self.b, 'The list is NOT sorted after merge sort reverse!')

    def test_heap_sort(self):
        comparison_sorting.heap_sort(self.b)
        list.sort(self.a)
        self.assertEqual(self.a, self.b, 'The list is NOT sorted after heap sort!')

    def test_heap_sort_reverse(self):
        comparison_sorting.heap_sort(self.b, reverse=True)
        list.sort(self.a, reverse=True)
        self.assertEqual(self.a, self.b, 'The list is NOT sorted after heap sort reverse!')

    def test_quick_sort(self):
        comparison_sorting.quick_sort(self.b)
        list.sort(self.a)
        self.assertEqual(self.a, self.b, 'The list is NOT sorted after quick sort!')

    def test_quick_sort_reverse(self):
        comparison_sorting.quick_sort(self.b, reverse=True)
        list.sort(self.a, reverse=True)
        self.assertEqual(self.a, self.b, 'The list is NOT sorted after quick sort reverse!')

    def test_quick_sort_rd(self):
        comparison_sorting.quick_sort(self.b, randomized_partition=True)
        list.sort(self.a)
        self.assertEqual(self.a, self.b, 'The list is NOT sorted after quick sort!')

    def test_quick_sort_reverse_rd(self):
        comparison_sorting.quick_sort(self.b, reverse=True, randomized_partition=True)
        list.sort(self.a, reverse=True)
        self.assertEqual(self.a, self.b, 'The list is NOT sorted after quick sort reverse!')

    def test_sort_random_list(self):
        t = 1000
        a = [random.randint(t * -1, t) for _ in range(t)]

        a_straight_insertion_sort = copy.deepcopy(a)
        comparison_sorting.straight_insertion_sort(a_straight_insertion_sort)

        a_two_way_insertion_sort = copy.deepcopy(a)
        comparison_sorting.two_way_insertion_sort(a_two_way_insertion_sort)

        a_merge_sort = copy.deepcopy(a)
        comparison_sorting.merge_sort(a_merge_sort)

        a_heap_sort = copy.deepcopy(a)
        comparison_sorting.heap_sort(a_heap_sort)

        a_quick_sort = copy.deepcopy(a)
        comparison_sorting.quick_sort(a_quick_sort)

        list.sort(a)

        self.assertEqual(a, a_straight_insertion_sort, 'The list is NOT sorted after straight insertion sort!')
        self.assertEqual(a, a_two_way_insertion_sort, 'The list is NOT sorted after two way insertion sort!')
        self.assertEqual(a, a_merge_sort, 'The list is NOT sorted after merge sort!')
        self.assertEqual(a, a_heap_sort, 'The list is NOT sorted after heap sort!')
        self.assertEqual(a, a_quick_sort, 'The list is NOT sorted after quick sort!')

    def test_sort_random_list_reverse(self):
        t = 1000
        a = [random.randint(t * -1, t) for _ in range(t)]

        a_straight_insertion_sort = copy.deepcopy(a)
        comparison_sorting.straight_insertion_sort(a_straight_insertion_sort, reverse=True)

        a_two_way_insertion_sort = copy.deepcopy(a)
        comparison_sorting.two_way_insertion_sort(a_two_way_insertion_sort, reverse=True)

        a_merge_sort = copy.deepcopy(a)
        comparison_sorting.merge_sort(a_merge_sort, reverse=True)

        a_heap_sort = copy.deepcopy(a)
        comparison_sorting.heap_sort(a_heap_sort, reverse=True)

        a_quick_sort = copy.deepcopy(a)
        comparison_sorting.quick_sort(a_quick_sort, reverse=True)

        list.sort(a, reverse=True)

        self.assertEqual(a, a_straight_insertion_sort, 'The list is NOT sorted after straight insertion sort reverse!')
        self.assertEqual(a, a_two_way_insertion_sort, 'The list is NOT sorted after two way insertion sort reverse!')
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
        comparison_sorting._merge(actual, p, q, r)
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
        comparison_sorting._merge(actual, p, q, r, reverse=True)
        expect = a[p:r + 1]
        list.sort(expect, reverse=True)

        self.assertEqual(expect, actual[p:r + 1],
                         'The %d to %d items in list is NOT sorted after merge reverse!' % (p, r + 1))
