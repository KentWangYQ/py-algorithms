# coding=utf-8

import unittest
from tree import bst

""" demo tree
         7
        / \
       5   8
      / \   \
     2  6    9
"""
demo_tree = bst.BSTree(keys=[7, 5, 2, 6, 8, 9])


class BSTTest(unittest.TestCase):
    """
    二叉搜索树测试
    """

    def test_insert_node(self):
        """
        插入结点测试
        :return:
        """
        new_node = bst.Node(key=3)
        demo_tree.insert_node(new_node)
        bst.inorder_tree_walk_recursive(demo_tree.root)

    def test_tree_walk(self):
        """
        中序遍历测试
        :return:
        """
        bst.inorder_tree_walk_recursive(demo_tree.root)
        print('----------------')
        bst.inorder_tree_walk_stack(demo_tree.root)
        print('----------------')
        bst.inorder_tree_walk_pointer(demo_tree.root)

    def test_tree_search(self):
        """
        搜索测试
        :return:
        """
        key = 8
        # result = tree_search(demo_tree.root, key)
        result = bst.iterative_tree_search(demo_tree.root, key)
        if result:
            print('result key: %s' % result.key)
        else:
            print('result key: %s NOT FOUND' % key)

        minimum = bst.tree_minimum(demo_tree.root)
        if minimum:
            print('minimum: %s' % minimum.key)
        else:
            print('Tree is None')

        maximum = bst.tree_maximum(demo_tree.root)
        if maximum:
            print('maximum: %s' % maximum.key)
        else:
            print('Tree is None')

        node = demo_tree.root.left
        successor = bst.tree_successor(node)
        if successor:
            print('Node %s\'s successor is: %s' % (node.key, successor.key))
        else:
            print('Tree is None')

        predecessor = bst.tree_predecessor(demo_tree.root.left)
        if predecessor:
            print('Node %s\'s predecessor is: %s' % (node.key, predecessor.key))
        else:
            print('Tree is None')

    def test_transplant(self):
        """
        结点替换测试
        :return:
        """
        new_tree = bst.transplant(demo_tree, demo_tree.root.left, bst.tree_successor(demo_tree.root.left))
        bst.inorder_tree_walk_recursive(new_tree.root)

    def test_delete_node(self):
        """
        删除结点测试
        :return:
        """
        demo_tree.delete_node(demo_tree.root)
        bst.inorder_tree_walk_recursive(demo_tree.root)
