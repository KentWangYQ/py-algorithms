# -*- coding: utf-8 -*-

import unittest
import random

from source.sorting import linear_time_sorting


class LinearTimeSortingTest(unittest.TestCase):
    def setUp(self):
        self.a = [100, 62, 5426, 34356, 503, 46, 0, 313569, 187, 85, 6, 5400]
        self.max = max(self.a)
        self.d = len(str(self.max))

    def test_counting_sort(self):
        counting_sort_result = linear_time_sorting.counting_sort(self.a, self.max)
        list.sort(self.a)
        self.assertEqual(self.a, counting_sort_result, 'The list is NOT sorted after counting sort!')

    def test_counting_sort_reverse(self):
        counting_sort_reverse_result = linear_time_sorting.counting_sort(self.a, self.max, reverse=True)
        list.sort(self.a, reverse=True)
        self.assertEqual(self.a, counting_sort_reverse_result, 'The list is NOT sorted after counting sort reverse!')

    # 基数排序测试
    def test_radix_sort(self):
        """
        基数排序测试
        :return:
        """
        radix_sort_result = linear_time_sorting.radix_sort(self.a, self.d)
        list.sort(self.a)
        self.assertEqual(self.a, radix_sort_result, 'The list is NOT sorted after radix sort!')

    # 基数排序倒序测试
    def test_radix_sort_reverse(self):
        """
        基数排序倒序测试
        :return:
        """
        radix_sort_reverse_result = linear_time_sorting.radix_sort(self.a, self.d, reverse=True)
        list.sort(self.a, reverse=True)
        self.assertEqual(self.a, radix_sort_reverse_result, 'The list is NOT sorted after radix sort reverse!')

    def test_bucket_sort(self):
        a = [v / (self.max + 1) for v in self.a]
        bucket_sort_result = linear_time_sorting.bucket_sort(a)
        list.sort(a)
        self.assertEqual(a, bucket_sort_result, 'The list is NOT sorted after bucket sort!')

    def test_bucket_sort_reverse(self):
        a = [v / (self.max + 1) for v in self.a]
        bucket_sort_reverse_result = linear_time_sorting.bucket_sort(a, reverse=True)
        list.sort(a, reverse=True)
        self.assertEqual(a, bucket_sort_reverse_result, 'The list is NOT sorted after bucket sort reverse!')

    def test_sort_random_list(self):
        t = 1000
        a = [random.randint(0, t * 100) for _ in range(t)]
        _max = max(a)
        d = len(str(max))

        b = [v / (_max + 1) for v in a]

        counting_sort_result = linear_time_sorting.counting_sort(a, _max)
        radix_sort_result = linear_time_sorting.radix_sort(a, d)
        bucket_sort_result = linear_time_sorting.bucket_sort(b)

        list.sort(a)
        list.sort(b)

        self.assertEqual(a, counting_sort_result, 'The list is NOT sorted after counting sort!')
        self.assertEqual(a, radix_sort_result, 'The list is NOT sorted after radix sort!')
        self.assertEqual(b, bucket_sort_result, 'The list is NOT sorted after bucket sort!')

    def test_sort_random_list_reverse(self):
        t = 1000
        a = [random.randint(0, t * 100) for _ in range(t)]
        _max = max(a)
        d = len(str(_max))

        b = [v / (_max + 1) for v in a]

        counting_sort_reverse_result = linear_time_sorting.counting_sort(a, _max, True)
        radix_sort_reverse_result = linear_time_sorting.radix_sort(a, d, True)
        bucket_sort_reverse_result = linear_time_sorting.bucket_sort(b, True)

        list.sort(a, reverse=True)
        list.sort(b, reverse=True)

        self.assertEqual(a, counting_sort_reverse_result, 'The list is NOT sorted after counting sort reverse!')
        self.assertEqual(a, radix_sort_reverse_result, 'The list is NOT sorted after radix sort reverse!')
        self.assertEqual(b, bucket_sort_reverse_result, 'The list is NOT sorted after bucket sort reverse!')
