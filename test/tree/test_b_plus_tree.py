# -*- coding: utf-8 -*-

import unittest
import random
from source.tree.b_plus_tree import BPNode, BPTree


class BPTreeTest(unittest.TestCase):
    def test_split_node(self):
        keys = [1, 3, 9, 12, 56]
        tree = BPTree(t=3)
        tree.root.is_leaf = False
        tree.root.append_key(1)
        node = BPNode(t=tree.t, is_leaf=True)
        for key in keys:
            node.append_key(key)
            node.append_value(key)
        tree.root.append_c(node)
        tree._split_node(tree.root, 0)

        self.assertEqual([1, 9], [key for key in tree.root.keys if key is not None],
                         'Parent node keys do NOT match with expect after split node!')
        self.assertEqual([1, 3], [key for key in tree.root.c[0].keys if key is not None],
                         'Left node keys do NOT match with expect after split node!')
        self.assertEqual([1, 3], [value for value in tree.root.c[0].values if value is not None],
                         'Left node values do NOT match with expect after split node!')
        self.assertEqual([9, 12, 56], [key for key in tree.root.c[1].keys if key is not None],
                         'Right node keys do NOT match with expect after split node!')
        self.assertEqual([9, 12, 56], [value for value in tree.root.c[1].values if value is not None],
                         'Right node values do NOT match with expect after split node!')

    def test_insert(self):
        keys = []
        for _ in range(1000):
            keys.append(random.randint(0, 1000))

        tree = BPTree(t=5)
        for key in keys:
            tree.insert(key, key)

        list.sort(keys)
        expect = keys
        actual = tree.tree_walk()
        self.assertEqual(expect, actual, 'The tree is NOT a b-plus-tree after insert keys!')

    def test_tree_walk(self):
        keys = [6, 4, 56, 8, 13, 54, 66, 48, 135, 486, 5, 65, 12, 456, 85, 431, 6614, 9646, 46, 11, 6594, 5648, 1]
        tree = b_plus_tree_generate(keys=keys)

        list.sort(keys)
        expect = keys
        actual = tree.tree_walk()
        self.assertEqual(expect, actual, 'Tree walk provide wrong result!')


def b_plus_tree_generate(t=3, max_key=20, keys=None):
    tree = BPTree(t=t)

    if keys:
        for key in keys:
            tree.insert(key, key)
    elif max_key:
        for i in range(max_key):
            tree.insert(i, i)

    return tree
