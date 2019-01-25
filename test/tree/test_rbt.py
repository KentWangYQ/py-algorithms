# coding=utf-8

import unittest
from tree import bst, avl, rbt


class RBTreeTest(unittest.TestCase):
    def test_left_rotate(self):
        rr_tree = rbt.RBTree(root=bst.BSTree(keys=[7, 4, 10, 8, 15, 12]).root)
        self.assertGreaterEqual(abs(avl.balance_factor(rr_tree.root)), 2, 'The rr tree is NOT a NON balance tree!')
        rr_tree.left_rotate(rr_tree.root)
        self.assertLess(avl.balance_factor(rr_tree.root), 2, 'The rr tree do NOT balance after right rotate!')

    def test_right_rotate(self):
        ll_tree = rbt.RBTree(root=bst.BSTree(keys=[7, 4, 3, 5, 1, 8]).root)
        self.assertGreaterEqual(abs(avl.balance_factor(ll_tree.root)), 2, 'The ll tree is NOT a NON balance tree!')
        ll_tree.right_rotate(ll_tree.root)
        self.assertLess(avl.balance_factor(ll_tree.root), 2, 'The ll tree do NOT balance after left rotate!')
