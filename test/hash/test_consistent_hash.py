# -*- coding: utf-8 -*-

import unittest

from source.hash import consistent_hash


class ConsistentHashTest(unittest.TestCase):
    def setUp(self):
        self.NODE_COUNT = 100
        self.V = 10
        self.ITEM_COUNT = 1000000

    def test_normal_hash(self):
        """
        普通hash分布算法测试
        :return:
        """
        print('==== Normal hash test ====')
        consistent_hash.normal_hash(self.NODE_COUNT, self.ITEM_COUNT)

    def test_consistent_hash(self):
        """
        一致性Hash算法测试
        :return:
        """
        print('==== Consistent hash test ====')
        consistent_hash.consistent_hash(self.NODE_COUNT, self.ITEM_COUNT)

    def test_consistent_hash_vnode(self):
        """
        一致性Hash算法(虚拟结点)测试
        :return:
        """
        print('==== Consistent hash vnode test ====')
        consistent_hash.consistent_hash_vnode(self.NODE_COUNT, self.V, self.ITEM_COUNT)
