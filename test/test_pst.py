# coding=utf-8

import unittest
from tree import pst

demo_tree = pst.create_tree([7, 5, 2, 6, 8, 9])


class PSTTest(unittest.TestCase):
    def test_tree_insert(self):
        """
        插入结点测试
        :return:
        """
        new_node = pst.Node(key=3)
        new_tree = pst.tree_insert(demo_tree, new_node)
        pst.inorder_tree_walk_recursive(new_tree.root)

    def test_tree_walk(self):
        """
        中序遍历测试
        :return:
        """
        pst.inorder_tree_walk_recursive(demo_tree.root)
        print('----------------')
        pst.inorder_tree_walk_stack(demo_tree.root)
        print('----------------')
        pst.inorder_tree_walk_pointer(demo_tree.root)

    def test_tree_search(self):
        """
        搜索测试
        :return:
        """
        key = 8
        # result = tree_search(demo_tree.root, key)
        result = pst.iterative_tree_search(demo_tree.root, key)
        if result:
            print('result key: %s' % result.key)
        else:
            print('result key: %s NOT FOUND' % key)

        minimum = pst.tree_minimum(demo_tree.root)
        if minimum:
            print('minimum: %s' % minimum.key)
        else:
            print('Tree is None')

        maximum = pst.tree_maximum(demo_tree.root)
        if maximum:
            print('maximum: %s' % maximum.key)
        else:
            print('Tree is None')

        node = demo_tree.root.left
        successor = pst.tree_successor(node)
        if successor:
            print('Node %s\'s successor is: %s' % (node.key, successor.key))
        else:
            print('Tree is None')

        predecessor = pst.tree_predecessor(demo_tree.root.left)
        if predecessor:
            print('Node %s\'s predecessor is: %s' % (node.key, predecessor.key))
        else:
            print('Tree is None')

    def test_transplant(self):
        new_tree = pst.transplant(demo_tree, demo_tree.root.left, pst.tree_successor(demo_tree.root.left))
        pst.inorder_tree_walk_recursive(new_tree.root)

    def test_tree_delete(self):
        new_tree = pst.tree_delete(demo_tree, demo_tree.root)
        pst.inorder_tree_walk_recursive(new_tree.root)
