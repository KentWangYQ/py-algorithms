# coding=utf-8

import unittest

from tree.node import Node
from tree import bst, avl

""" demo tree
         7
        / \
       5   8
      / \   \
     2  6    9
    /
   1
"""
demo_tree = bst.Tree(keys=[7, 5, 2, 1, 6, 8, 9])

""" ll tree
         7
        / \
       4   8
      / \   
     3  5    
    /
   1
"""
ll_tree = bst.Tree(keys=[7, 4, 3, 5, 1, 8])

""" rr tree
         7
        / \
       4   10
           / \
          8  15
            / 
           12
"""
rr_tree = bst.Tree(keys=[7, 4, 10, 8, 15, 12])

""" lr tree
         7
        / \
       4   8
      / \   
     2   6    
        /   
       5
"""
lr_tree = bst.Tree(keys=[7, 4, 2, 6, 5, 8])

""" rl tree
         7
        / \
       4   12
           / \
          10 14
          / 
         9
"""
rl_tree = bst.Tree(keys=[7, 4, 12, 10, 9, 14])


class AVLTest(unittest.TestCase):
    """
    二叉平衡树测试
    """

    def test_node_height(self):
        """
        树高测试
        :return:
        """
        height = avl.node_height(demo_tree.root)
        self.assertEqual(4, height, 'node height wrong!')

    def test_balance_factor(self):
        """
        平衡因子测试
        :return:
        """
        factor = avl.balance_factor(demo_tree.root)
        self.assertEqual(1, factor, 'balance factor wrong!')

    def test_left_rotate(self):
        """
        左旋测试
        :return:
        """
        self.assertGreaterEqual(abs(avl.balance_factor(rr_tree.root)), 2,
                                'rr_tree is not a NON balance tree!')
        self.assertLess(abs(avl.balance_factor(avl.left_rotate(rr_tree.root))), 2,
                        'rr_tree is NOT balance after right_rotate!')

    def test_right_rotate(self):
        """
        右旋测试
        :return:
        """
        self.assertGreaterEqual(abs(avl.balance_factor(ll_tree.root)), 2,
                                'll_tree is not a NON balance tree!')
        self.assertLess(abs(avl.balance_factor(avl.right_rotate(ll_tree.root))), 2,
                        'll_tree is NOT balance after left_rotate!')

    def test_left_right_rotate(self):
        """
        左右旋测试
        :return:
        """
        self.assertGreaterEqual(abs(avl.balance_factor(rl_tree.root)), 2,
                                'rl_tree is not a NON balance tree!')
        self.assertLess(abs(avl.balance_factor(avl.left_right_rotate(rl_tree.root))), 2,
                        'rl_tree is NOT balance after left_right_rotate!')

    def test_right_left_rotate(self):
        """
        右左旋测试
        :return:
        """
        self.assertGreaterEqual(abs(avl.balance_factor(lr_tree.root)), 2,
                                'lr_tree is not a NON balance tree!')
        self.assertLess(abs(avl.balance_factor(avl.right_left_rotate(lr_tree.root))), 2,
                        'rl_tree is not a NON balance tree!')

    def test_rebalance(self):
        """
        再平衡测试
        :return:
        """
        bst_tree = bst.Tree(keys=[7, 4, 12, 10, 9, 14])
        t = avl.Tree(root=bst_tree.root)
        self.assertGreaterEqual(abs(avl.balance_factor(t.root)), 2, 'The tree has already balance!')
        t.rebalance()
        self.assertLess(abs(avl.balance_factor(t.root)), 2, 'The tree do NOT balance after rebalance!')

    def test_insert_node(self):
        """
        插入新节点
        :return:
        """
        bst_tree = bst.Tree(keys=[7, 4, 12, 10, 9, 14])
        t = avl.Tree(root=bst_tree.root)
        t.insert_node(Node(key=8))
        self.assertLess(abs(avl.balance_factor(t.root)), 2, 'The tree do NOT balance after insert node!')

    def test_delete_node(self):
        """
        删除结点
        :return:
        """
        bst_tree = bst.Tree(keys=[7, 4, 12, 10, 9, 14])
        t = avl.Tree(root=bst_tree.root)
        t.delete_node(t.root.left)
        self.assertLess(abs(avl.balance_factor(t.root)), 2, 'The tree do NOT balance after delete node!')
