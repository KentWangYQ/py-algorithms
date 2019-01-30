# coding=utf-8

import unittest
from tree.bt import BNode, BTree


class BTreeTest(unittest.TestCase):
    def test_create(self):
        """
        创建B-Tree测试
        :return:
        """
        r = BTree()
        r.create()
        self.assertIsInstance(r.root, BNode, 'The root of tree is NOT instance of BNode!')

    def test_insert(self):
        """
        插入新结点测试
        :return:
        """
        r = BTree(t=2)
        r.create()
        for i in range(10, 0, -1):
            r.insert(i)

        expect = [7, 3, 5, 9, 1, 2, 4, 6, 8, 10]
        actual = []
        nodes = [r.root]
        while True:
            if len(nodes) > 0:
                n = nodes[0]
                del nodes[0]
                actual += [k for k in n.keys if k]
                nodes += [c for c in n.c if c]
            else:
                break

        self.assertEqual(expect, actual, 'The tree is not created in B-Tree role!')

    def test_search(self):
        """
        键搜索测试
        :return:
        """
        r = BTree(t=2)
        r.create()
        for i in range(10, 0, -1):
            r.insert(i)

        # 键存在
        x, i = r.search(r.root, 2)
        self.assertEqual((x, i), (r.root.c[0].c[0], 1), 'The result is NOT for key: %s' % 2)

        # 键不存在
        x = r.search(r.root, 11)
        self.assertIsNone(x, 'There is NO key %s in tree, but found!' % 11)
