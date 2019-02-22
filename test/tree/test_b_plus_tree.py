# -*- coding: utf-8 -*-

import unittest
import random
from source.tree import b_plus_tree
from source.tree.b_plus_tree import BPNode, BPTree


class BPTreeTest(unittest.TestCase):
    def test_tree_walk(self):
        keys = [6, 4, 56, 8, 13, 54, 66, 48, 135, 486, 5, 65, 12, 456, 85, 431, 6614, 9646, 46, 11, 6594, 5648, 1]
        tree = b_plus_tree_generate(keys=keys)

        list.sort(keys)
        expect = keys
        actual = tree.tree_walk()
        self.assertEqual(expect, actual, 'Tree walk provide wrong result!')

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

    def test_merge_node(self):
        tree = BPTree(t=3)
        tree.root.is_leaf = False
        for key in [1, 4, 6]:
            tree.root.append_key(key)

        n1 = BPNode(t=3)
        for key in [1, 2, 3]:
            n1.append_key(key)

        n2 = BPNode(t=3)
        for key in [4, 5]:
            n2.append_key(key)

        n3 = BPNode(t=3)
        for key in [6, 7]:
            n3.append_key(key)

        for n in [n1, n2, n3]:
            tree.root.append_c(n)
        tree._merge_node(tree.root, 1)
        self.assertEqual([[1, 2, 3, 4, 5], [6, 7]],
                         [[key for key in c.keys if key is not None] for c in tree.root.c if c],
                         'Children node keys wrong after merge node!')

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

    def test_delete(self):
        tree = b_plus_tree_generate(t=3, max_key=20)

        del_key = 8
        tree.delete(tree.root, del_key)

        self.assertEqual([i for i in range(20) if i != del_key], tree.tree_walk(),
                         'The tree has WRONG keys after delete key!')

    def test_search(self):
        tree = b_plus_tree_generate(t=3, max_key=20)

        self.assertEqual((tree.root.c[0].c[1], 2), b_plus_tree.search(tree.root, 6),
                         'Search result is NOT match with the expect!')

        self.assertEqual((None, -1), b_plus_tree.search(tree.root, 21), 'Search result is NOT match the expect!')

    def test_random_insert_delete_test(self):
        for i in range(100):
            print('Round: %d' % i)

            n = 1000
            keys = []
            tree = BPTree(t=5)

            for _ in range(n):
                key = random.randint(1, n * 10)
                keys.append(key)

            for key in keys:
                tree.insert(key, key)

            list.sort(keys)

            self.assertEqual(keys, tree.tree_walk(), 'The tree is NOT a b-plus-tree after insert keys!')

            for _ in range(n // 3):
                i = random.randint(0, len(keys) - 1)

                x1, j1 = b_plus_tree.search(tree.root, keys[i])
                self.assertEqual(x1.keys[j1], keys[i], 'The search result does NOT match expect!')

                tree.delete(tree.root, keys[i])
                del keys[i]
                self.assertEqual(keys, tree.tree_walk(), 'The tree has WRONG keys after delete key!')


def b_plus_tree_generate(t=3, max_key=20, keys=None):
    tree = BPTree(t=t)

    if keys:
        for key in keys:
            tree.insert(key, key)
    elif max_key:
        for i in range(max_key):
            tree.insert(i, i)

    return tree
