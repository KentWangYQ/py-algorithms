# coding=utf-8

import unittest
from source.tree import bst, avl, rbt


class RBTreeTest(unittest.TestCase):
    def test_left_rotate(self):
        """
        左旋测试
        :return:
        """
        rr_tree = rbt.RBTree(root=bst.BSTree(keys=[7, 4, 10, 8, 15, 12]).root)
        self.assertGreaterEqual(abs(avl.balance_factor(rr_tree.root)), 2, 'The rr tree is NOT a NON balance tree!')
        rr_tree.left_rotate(rr_tree.root)
        self.assertLess(avl.balance_factor(rr_tree.root), 2, 'The rr tree do NOT balance after right rotate!')

    def test_right_rotate(self):
        """
        右旋测试
        :return:
        """
        ll_tree = rbt.RBTree(root=bst.BSTree(keys=[7, 4, 3, 5, 1, 8]).root)
        self.assertGreaterEqual(abs(avl.balance_factor(ll_tree.root)), 2, 'The ll tree is NOT a NON balance tree!')
        ll_tree.right_rotate(ll_tree.root)
        self.assertLess(avl.balance_factor(ll_tree.root), 2, 'The ll tree do NOT balance after left rotate!')

    def test_insert_fixup(self):
        """
        红黑树修复测试
        :return:
        """
        tree = rbt.RBTree(keys=[11, 2, 1, 7, 5, 8, 14, 15])
        self.assertIs(tree.check(), True, 'The tree is NOT a RB tree!')
        node = rbt.RBNode(key=4)
        p = tree.root.left.right
        if p:
            p.left = node
            node.parent = p
        self.assertIs(tree.check(), True, 'The tree is NOT a RB tree after insert_fixup!')

    def test_insert(self):
        """
        插入新节点测试
        :return:
        """
        tree = rbt.RBTree()
        keys = [8, 15, 2, 6, 12, 9, 6, 20, 10, 4]
        for key in keys:
            tree.insert_node(rbt.RBNode(key=key))
        self.assertIs(tree.check(), True, 'The tree is NOT a RB tree after insert new node!')

    def test_delete_fixup(self):
        pass

    def test_delete(self):
        tree = rbt.RBTree(keys=[8, 15, 2, 12, 4, 9, 6, 20, 10])
        self.assertIs(tree.check(), True, 'The tree is NOT a RB tree!')
        tree.delete(tree.root.right)
        self.assertIs(tree.check(), True, 'The tree is NOT a RB tree after delete node!')
