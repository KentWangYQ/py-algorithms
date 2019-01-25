# coding=utf-8

from enum import Enum

from tree.bst import BSTree
from tree.node import Node


class COLOR(Enum):
    red = 'red'
    black = 'black'


class RBNode(Node):
    def __init__(self, key, color=COLOR.red):
        super().__init__(key=key)
        self.color = color


class RBTree(BSTree):
    nil = RBNode(key=None, color=COLOR.black)

    def __init__(self, root, keys=None):
        super().__init__(root=root, keys=keys)

    def left_rotate(self, node):
        a = node  # type: RBNode
        b = node.right  # type: RBNode

        a.right = b.left
        if b.left:
            b.left.parent = a

        b.left = a
        b.parent = a.parent
        a.parent = b

        if not b.parent:
            self.root = b

    def right_rotate(self, node):
        a = node  # type: RBNode
        b = node.left  # type: RBNode

        a.left = b.right
        if b.right:
            b.right.parent = a

        b.right = a
        b.parent = a.parent
        a.parent = b

        if not b.parent:
            self.root = b

    def fixup(self, z):
        while z.parent.color == COLOR.red:
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right
                if y.color == COLOR.red:
                    z.p.color = COLOR.black
                    y.color = COLOR.black
                    z.parent.parent.color = COLOR.red
                    z = z.parent.parent
                elif z == z.parent.right:
                    z = z.parent
                    self.left_rotate(z)
                z.parent.color = COLOR.black
                z.parent.parent.color = COLOR.red
                self.right_rotate(z.parent.parent)
            else:
                pass
        self.root.color = COLOR.black
