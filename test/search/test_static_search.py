# -*- coding: utf-8 -*-

import unittest

from source.search import static_search


class StaticSearchTest(unittest.TestCase):
    def setUp(self):
        self.a = [3, 2, -20, 309, -987, 2, 487, -20, 90, -5, 0, 98]
        self.key = 309

    def test_sequential_search(self):
        expect = 3, self.key
        actual = static_search.sequential_search(self.a, self.key)
        self.assertEqual(expect, actual, 'The result from sequential search is NOT match with expect!')

    def test_binary_search(self):
        expect = 10, self.key
        list.sort(self.a)
        actual = static_search.binary_search(self.a, self.key)
        self.assertEqual(expect, actual, 'The result from binary search is NOT match with expect!')
