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

    # region INSERTION SORT TEST
    # 直接插入排序测试
    def test_straight_insertion_sort(self):
        """
        直接插入排序测试
        :return:
        """
        comparison_sorting.straight_insertion_sort(self.b)
        list.sort(self.a)
        self.assertEqual(self.a, self.b, 'The list is NOT sorted after straight insertion sort!')

    # 直接插入排序倒序测试
    def test_straight_insertion_sort_reverse(self):
        """
        直接插入排序倒序测试
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

    # 折半插入排序倒序测试
    def test_binary_insertion_sort_reverse(self):
        """
        折半插入排序倒序测试
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

    # 2路插入排序倒序测试
    def test_two_way_insertion_sort_reverse(self):
        """
        2路插入排序倒序测试
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

    # 表插入排序倒序测试
    def test_list_insertion_sort_reverse(self):
        """
        表插入排序倒序测试
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

    # 希尔排序测试
    def test_shell_sort(self):
        """
        希尔排序测试
        :return:
        """
        comparison_sorting.shell_sort(self.b, [5, 3, 1])
        list.sort(self.a)
        self.assertEqual(self.a, self.b, 'The list is NOT sorted after shell sort!')

    # 希尔排序倒序测试
    def test_shell_sort_reverse(self):
        """
        希尔排序倒序测试
        :return:
        """
        comparison_sorting.shell_sort(self.b, [6, 4, 2, 1], True)
        list.sort(self.a, reverse=True)
        self.assertEqual(self.a, self.b, 'The list is NOT sorted after shell sort reverse!')

    # endregion

    # region QUICK SORT TEST

    # 冒泡排序测试
    def test_bubble_sort(self):
        """
        冒泡排序测试
        :return:
        """
        comparison_sorting.bubble_sort(self.b)
        list.sort(self.a)
        self.assertEqual(self.a, self.b, 'The list is NOT sorted after bubble sort!')

    # 冒泡排序倒序测试
    def test_bubble_sort_reverse(self):
        """
        冒泡排序倒序测试
        :return:
        """
        comparison_sorting.bubble_sort(self.b, True)
        list.sort(self.a, reverse=True)
        self.assertEqual(self.a, self.b, 'The list is NOT sorted after bubble sort reverse!')

    # 快速排序测试
    def test_quick_sort(self):
        """
        快速排序测试
        :return:
        """
        comparison_sorting.quick_sort(self.b)
        list.sort(self.a)
        self.assertEqual(self.a, self.b, 'The list is NOT sorted after quick sort!')

    # 快速排序倒序测试
    def test_quick_sort_reverse(self):
        """
        快速排序倒序测试
        :return:
        """
        comparison_sorting.quick_sort(self.b, reverse=True)
        list.sort(self.a, reverse=True)
        self.assertEqual(self.a, self.b, 'The list is NOT sorted after quick sort reverse!')

    # 快速排序随机分割策略测试
    def test_quick_sort_rd(self):
        """
        快速排序随机分割策略测试
        :return:
        """
        comparison_sorting.quick_sort(self.b, randomized_partition=True)
        list.sort(self.a)
        self.assertEqual(self.a, self.b, 'The list is NOT sorted after quick sort!')

    # 快速排序随机分割策略倒序测试
    def test_quick_sort_reverse_rd(self):
        """
        快速排序随机分割策略倒序测试
        :return:
        """
        comparison_sorting.quick_sort(self.b, reverse=True, randomized_partition=True)
        list.sort(self.a, reverse=True)
        self.assertEqual(self.a, self.b, 'The list is NOT sorted after quick sort reverse!')

    # endregion

    # region SELECT SORT TEST

    def test_simple_selection_sort(self):
        comparison_sorting.simple_selection_sort(self.b)
        list.sort(self.a)
        self.assertEqual(self.a, self.b, 'The list is NOT sorted after simple selection sort!')

    def test_simple_selection_sort_reverse(self):
        comparison_sorting.simple_selection_sort(self.b, True)
        list.sort(self.a, reverse=True)
        self.assertEqual(self.a, self.b, 'The list is NOT sorted after simple selection sort reverse!')

    def test_tree_selection_sort(self):
        a_tree_selection_sort_result = comparison_sorting.tree_selection_sort(self.a)
        list.sort(self.a)
        self.assertEqual(self.a, a_tree_selection_sort_result, 'The list is NOT sorted after tree selection sort!')

    def test_heap_sort(self):
        comparison_sorting.heap_sort(self.b)
        list.sort(self.a)
        self.assertEqual(self.a, self.b, 'The list is NOT sorted after heap sort!')

    def test_heap_sort_reverse(self):
        comparison_sorting.heap_sort(self.b, reverse=True)
        list.sort(self.a, reverse=True)
        self.assertEqual(self.a, self.b, 'The list is NOT sorted after heap sort reverse!')

    # endregion

    # region MERGE SORT

    # 合并有序序列测试
    def test_merge(self):
        """
        合并有序序列测试
        :return:
        """
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

    # 归并排序辅助方法测试
    def test__merge(self):
        """
        归并排序辅助方法测试
        :return:
        """
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

    # 归并排序测试
    def test_merge_sort(self):
        """
        归并排序测试
        :return:
        """
        comparison_sorting.merge_sort(self.b)
        list.sort(self.a)
        self.assertEqual(self.a, self.b, 'The list is NOT sorted after merge sort!')

    # 归并排序倒序测试
    def test_merge_sort_reverse(self):
        """
        归并排序倒序测试
        :return:
        """
        comparison_sorting.merge_sort(a=self.b, reverse=True)
        list.sort(self.a, reverse=True)
        self.assertEqual(self.a, self.b, 'The list is NOT sorted after merge sort reverse!')

    # endregion

    # region SORTING RANDOM TEST
    def test_sort_random_list(self):
        t = 1000
        a = [random.randint(t * -1, t) for _ in range(t)]

        # region INSERTION SORT
        a_straight_insertion_sort = copy.deepcopy(a)
        comparison_sorting.straight_insertion_sort(a_straight_insertion_sort)

        a_binary_insertion_sort = copy.deepcopy(a)
        comparison_sorting.binary_insertion_sort(a_binary_insertion_sort)

        a_two_way_insertion_sort = copy.deepcopy(a)
        comparison_sorting.two_way_insertion_sort(a_two_way_insertion_sort)

        a_list_insertion_sort = copy.deepcopy(a)
        comparison_sorting.list_insertion_sort(a_list_insertion_sort)

        a_shell_sort = copy.deepcopy(a)
        comparison_sorting.shell_sort(a_shell_sort, [10, 6, 3, 1])
        # endregion

        # region QUICK SORT
        a_bubble_sort = copy.deepcopy(a)
        comparison_sorting.bubble_sort(a_bubble_sort)

        a_quick_sort = copy.deepcopy(a)
        comparison_sorting.quick_sort(a_quick_sort)

        a_quick_sort_rd = copy.deepcopy(a)
        comparison_sorting.quick_sort(a_quick_sort_rd, randomized_partition=True)
        # endregion

        # region SELECTION SORT
        a_simple_selection_sort = copy.deepcopy(a)
        comparison_sorting.simple_selection_sort(a_simple_selection_sort)

        a_tree_selection_sort_result = comparison_sorting.tree_selection_sort(a)

        a_heap_sort = copy.deepcopy(a)
        comparison_sorting.heap_sort(a_heap_sort)
        # endregion

        # region MERGE SORT
        a_merge_sort = copy.deepcopy(a)
        comparison_sorting.merge_sort(a_merge_sort)
        # endregion

        list.sort(a)

        # INSERTION SORT
        self.assertEqual(a, a_straight_insertion_sort, 'The list is NOT sorted after straight insertion sort!')
        self.assertEqual(a, a_binary_insertion_sort, 'The list is NOT sorted after binary insertion sort!')
        self.assertEqual(a, a_two_way_insertion_sort, 'The list is NOT sorted after two way insertion sort!')
        self.assertEqual(a, a_list_insertion_sort, 'The list is NOT sorted after list insertion sort!')
        self.assertEqual(a, a_shell_sort, 'The list is NOT sorted after shell sort!')

        # QUICK SORT
        self.assertEqual(a, a_bubble_sort, 'The list is NOT sorted after bubble sort!')
        self.assertEqual(a, a_quick_sort, 'The list is NOT sorted after quick sort!')
        self.assertEqual(a, a_quick_sort_rd, 'The list is NOT sorted after quick sort rd!')

        # SELECTION SORT
        self.assertEqual(a, a_simple_selection_sort, 'The list is NOT sorted after simple selection sort!')
        self.assertEqual(a, a_tree_selection_sort_result, 'The list is NOT sorted after tree selection sort!')
        self.assertEqual(a, a_heap_sort, 'The list is NOT sorted after heap sort!')

        # MERGE SORT
        self.assertEqual(a, a_merge_sort, 'The list is NOT sorted after merge sort!')

    def test_sort_random_list_reverse(self):
        t = 1000
        a = [random.randint(t * -1, t) for _ in range(t)]

        # region INSERTION SORT
        a_straight_insertion_sort = copy.deepcopy(a)
        comparison_sorting.straight_insertion_sort(a_straight_insertion_sort, reverse=True)

        a_binary_insertion_sort = copy.deepcopy(a)
        comparison_sorting.binary_insertion_sort(a_binary_insertion_sort, reverse=True)

        a_two_way_insertion_sort = copy.deepcopy(a)
        comparison_sorting.two_way_insertion_sort(a_two_way_insertion_sort, reverse=True)

        a_list_insertion_sort = copy.deepcopy(a)
        comparison_sorting.list_insertion_sort(a_list_insertion_sort, reverse=True)

        a_shell_sort = copy.deepcopy(a)
        comparison_sorting.shell_sort(a_shell_sort, [10, 6, 3, 1], reverse=True)
        # endregion

        # region QUICK SORT
        a_bubble_sort = copy.deepcopy(a)
        comparison_sorting.bubble_sort(a_bubble_sort, reverse=True)

        a_quick_sort = copy.deepcopy(a)
        comparison_sorting.quick_sort(a_quick_sort, reverse=True)

        a_quick_sort_rd = copy.deepcopy(a)
        comparison_sorting.quick_sort(a_quick_sort_rd, reverse=True, randomized_partition=True)
        # endregion

        # region SELECTION SORT
        a_simple_selection_sort = copy.deepcopy(a)
        comparison_sorting.simple_selection_sort(a_simple_selection_sort, reverse=True)

        a_heap_sort = copy.deepcopy(a)
        comparison_sorting.heap_sort(a_heap_sort, reverse=True)
        # endregion

        # region MERGE SORT
        a_merge_sort = copy.deepcopy(a)
        comparison_sorting.merge_sort(a_merge_sort, reverse=True)
        # endregion

        list.sort(a, reverse=True)

        # INSERTION SORT
        self.assertEqual(a, a_straight_insertion_sort, 'The list is NOT sorted after straight insertion sort reverse!')
        self.assertEqual(a, a_binary_insertion_sort, 'The list is NOT sorted after binary insertion sort reverse!')
        self.assertEqual(a, a_two_way_insertion_sort, 'The list is NOT sorted after two way insertion sort reverse!')
        self.assertEqual(a, a_list_insertion_sort, 'The list is NOT sorted after list insertion sort reverse!')
        self.assertEqual(a, a_shell_sort, 'The list is NOT sorted after shell sort reverse!')

        # QUICK SORT
        self.assertEqual(a, a_bubble_sort, 'The list is NOT sorted after bubble sort reverse!')
        self.assertEqual(a, a_quick_sort, 'The list is NOT sorted after quick sort reverse!')
        self.assertEqual(a, a_quick_sort_rd, 'The list is NOT sorted after quick sort rd reverse!')

        # SELECTION SORT
        self.assertEqual(a, a_simple_selection_sort, 'The list is NOT sorted after simple selection sort reverse!')
        self.assertEqual(a, a_heap_sort, 'The list is NOT sorted after heap sort reverse!')

        # MERGE SORT
        self.assertEqual(a, a_merge_sort, 'The list is NOT sorted after merge sort reverse!')
    # endregion
