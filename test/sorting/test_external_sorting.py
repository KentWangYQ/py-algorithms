# -*- coding: utf-8 -*-

import unittest

from source.sorting import external_sorting


# 外部排序测试
class ExternalSortingTest(unittest.TestCase):
    def setUp(self):
        self.a = [
            [2, 4, 1, 6, 8],
            [12, 3, 6, 69, 4],
            [23, 22, 40],
            [90, 290, 307, 2],
            [0, 92, 1, 38, 2]
        ]
        self.b = [u for v in self.a for u in v]

    # 多路平衡归并排序测试
    def test_multi_ways_balance_merge_sort(self):
        """
        多路平衡归并排序测试
        :return:
        """
        mwbms_result = external_sorting.multi_ways_balance_merge_sort(self.a)
        list.sort(self.b)
        self.assertEqual(self.b, mwbms_result,
                         'The list is NOT sorted after multi-ways balance merge sort!')
