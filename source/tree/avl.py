# -*- coding: utf-8 -*-

from .node import Node
from .bst import BSTree


class AVLTree(BSTree):
    """
    AVL Tree
    继承自bst tree
    """

    def __init__(self, root=None, keys=None):
        super().__init__(root=root, keys=keys)

    def rebalance(self):
        """
        再平衡，迭代使用转换操作，直到树达到平衡
        :return:
        """
        while True:
            bf = balance_factor(self.root)
            if abs(bf) < 2:
                break

            if bf >= 2:
                if balance_factor(self.root.left) > 0:
                    # ll_tree
                    self.root = right_rotate(self.root)
                else:
                    # lr_tree
                    self.root = right_left_rotate(self.root)
            else:
                if balance_factor(self.root.right) < 0:
                    # rr_tree
                    self.root = left_rotate(self.root)
                else:
                    # rl_tree
                    self.root = left_right_rotate(self.root)

    def insert_node(self, node):
        """
        插入新节点，且保持平衡
        :param node:
        :return:
        """
        super().insert_node(node)
        self.rebalance()

    def delete_node(self, node):
        """
        删除结点，且保持平衡
        :param node:
        :return:
        """
        super().delete_node(node)
        self.rebalance()


def node_height(node):
    """
    树或子树的高
    :param node:
    :return:
    """
    height_l = 0
    height_r = 0

    if node:
        if node.left:
            height_l += node_height(node.left)
        if node.right:
            height_r += node_height(node.right)

    return max(height_l + 1, height_r + 1)


def balance_factor(node):
    """
    结点的平衡因子，左右子树高的差
    :param node:
    :return:
    """
    if node:
        return node_height(node.left) - node_height(node.right)

    return 0


def left_rotate(node):
    """
    单旋转 左旋
    :param node:
    :return:
    """
    a = node  # type: Node
    b = node.right  # type: Node

    a.right = b.left
    b.left = a
    return b


def right_rotate(node):
    """
    单旋转 右旋
    :param node:
    :return:
    """
    a = node  # type: Node
    b = node.left  # type: Node

    a.left = b.right
    b.right = a
    return b


def left_right_rotate(node):
    """
    双旋转 左右旋
    :param node:
    :return:
    """
    node.left = left_rotate(node.right)
    return right_rotate(node)


def right_left_rotate(node):
    """
    双旋转 右左旋
    :param node:
    :return:
    """
    node.right = right_rotate(node.left)
    return left_rotate(node)
