# -*- coding: utf-8 -*-

import unittest

from source.sorting import external_sorting


# 外部排序测试
class ExternalSortingTest(unittest.TestCase):
    def setUp(self):
        self.k = 6  # 假设内存工作区可容纳5条记录
        self.a = [51, 49, 39, 46, 38, 29, 14, 61, 15, 30, 1, 48, 52, 3, 63, 27, 4, 13, 89, 24, 46, 58, 33, 76]  # 原始待排序列
        self.b = [self.a[i: i + self.k] for i in range(0, len(self.a), self.k)]  # 拆分归并段

    # 多路平衡归并排序测试
    def test_multi_ways_balance_merge_sort(self):
        """
        多路平衡归并排序测试
        :return:
        """
        mwbms_result = external_sorting.multi_ways_balance_merge_sort(self.b)
        list.sort(self.a)
        self.assertEqual(self.a, mwbms_result, 'The list is NOT sorted after multi-ways balance merge sort!')

    def test_replacement_selection_sort(self):
        replacement_selection_sort_result = external_sorting.replacement_selection_sort(self.a, self.k)
        list.sort(self.a)
        self.assertEqual(self.a, replacement_selection_sort_result,
                         'The list is NOT sorted after replacement selection sort!')
