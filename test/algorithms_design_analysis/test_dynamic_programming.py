# -*- coding: utf-8 -*-

import unittest
from source.algorithms_design_analysis import dynamic_programming


class DynamicProgrammingTest(unittest.TestCase):
    def setUp(self):
        self.cut_rod_p = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
        self.cut_rod_n = 10

    def test_memoized_cut_rod(self):
        """
        待备忘录的自顶向下法测试
        :return:
        """
        expect = 30
        actual = dynamic_programming.memoized_cut_rod(self.cut_rod_p, self.cut_rod_n)
        self.assertEqual(expect, actual, 'The actual is NOT an optimal solution!')

    def test_bottom_up_cut_rod(self):
        """
        自底向上法测试
        :return:
        """
        expect = 30
        actual = dynamic_programming.bottom_up_cut_rod(self.cut_rod_p, self.cut_rod_n)
        self.assertEqual(expect, actual, 'The actual is NOT an optimal solution!')
