# coding=utf-8

from enum import Enum

from tree.bst import BSTree
from tree.node import Node


class COLOR(Enum):
    """
    红黑树色值
    """
    red = 'red'
    black = 'black'


class Nil(object):
    """
    哨兵，作为红黑树中的叶子结点，颜色为黑色，其他属性为Nil
    """
    left = None
    right = None
    parent = None
    key = None
    color = COLOR.black


class RBNode(Node):
    """
    红黑树结点，默认红色，left、right默认Nil
    """

    def __init__(self, key, color=COLOR.red):
        super().__init__(key=key)
        self.color = color
        self.parent = Nil
        self.left = Nil
        self.right = Nil


class RBTree(BSTree):
    """
    红黑树
    继承自 BSTree
    """

    def __init__(self, root=Nil, keys=None):
        """
        构造函数，根据root和keys生成红黑树
        :param root:
        :param keys:
        """
        self.root = root
        if keys:
            for key in keys:
                self.insert_node(RBNode(key=key))

    # 插入结点
    def insert_node(self, z):
        """
        插入结点
        :param z:
        :return:
        """
        x = self.root
        y = Nil
        while x and x != Nil:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right

        z.parent = y
        if y == Nil:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z

        self.insert_fixup(z)

    def left_rotate(self, x):
        """
        左旋
        :param x:
        :return:
        """
        y = x.right
        x.right = y.left
        if y.left and y.left != Nil:
            y.left.parent = x
        y.parent = x.parent
        if not x.parent:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, x):
        """
        右旋
        :param x:
        :return:
        """
        y = x.left
        x.left = y.right
        if y.right != Nil:
            y.right.parent = x
        y.parent = x.parent
        if not x.parent:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def insert_fixup(self, z):
        """
        修正红黑树
        添加或删除结点后，会造成树不再满足红黑树的性质，通过该方法来修正新树为红黑树
        :param z:
        :return:
        """
        while z.parent != Nil and z.parent.parent != Nil and z.parent.color == COLOR.red:  # 父结点为红色
            if z.parent == z.parent.parent.left:  # 父结点是祖父结点的左子结点
                y = z.parent.parent.right  # 叔父结点
                if y.color == COLOR.red:  # 叔父结点为红色
                    '''
                    情况一：父结点和叔父结点都为红色。
                    解决方案：父结点和叔父结点涂成黑色，祖父结点涂成红色，
                    当前结点指向祖父结点。此时转换成情况二。
                    '''
                    z.parent.color = COLOR.black  # 父结点涂成黑色
                    y.color = COLOR.black  # 叔父结点涂成黑色
                    z.parent.parent.color = COLOR.red  # 祖父结点涂成红色
                    z = z.parent.parent  # 当前结点指向祖父结点
                elif z == z.parent.right:
                    '''
                    情况二：父结点为红色，叔父结点为黑色，当前结点是父结点的右子结点。
                    解决方案：父结点作为当前结点，并以新当前结点为支点左旋。
                    '''
                    z = z.parent
                    self.left_rotate(z)
                else:
                    '''
                    情况三：父结点为红色，叔父结点为黑色，当前结点是父结点的右子结点。
                    解决方案：父结点变为黑色，祖父结点变为红色，以祖父结点为支点右旋。
                    '''
                    z.parent.color = COLOR.black
                    z.parent.parent.color = COLOR.red
                    self.right_rotate(z.parent.parent)
            else:
                y = z.parent.parent.left
                if y.color == COLOR.red:
                    '''情况一'''
                    z.parent.color = COLOR.black
                    y.color = COLOR.black
                    z.parent.parent.color = COLOR.red
                    z = z.parent
                elif z == z.parent.left:
                    '''情况二'''
                    z = z.parent
                    self.right_rotate(z)
                else:
                    '''情况三'''
                    z.parent.color = COLOR.black
                    z.parent.parent.color = COLOR.red
                    self.left_rotate(z.parent.parent)
        self.root.color = COLOR.black

    def check(self):
        """
        检查当前实例是否为红黑树
        :return:
        """
        # 注：构建RBNode时已经自动将所有结点的左右子结点设置为Nil，其中Nil为黑色，符合第三条，所有叶子结点都是黑色。

        # 第二条：检查根结点是否是黑色
        if self.root and self.root.color != COLOR.black:
            return False

        # 逐个结点检查
        return rb_check(self.root)

    def transplant(self, u, v):
        if u.parent == Nil:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v

        v.parent = u.parent

    def delete_fixup(self, x):
        while x != self.root and x.color == COLOR.black:
            if x == x.parent.left:
                w = x.parent.right
                if w.color == COLOR.red:
                    w.color = COLOR.black
                    x.parent.color = COLOR.red
                    self.left_rotate(x.parent)
                    w = x.parent.right
                if w.left.color == COLOR.black and w.right.color == COLOR.black:
                    w.color = COLOR.red
                    x = x.parent
                elif w.right.color == COLOR.black:
                    w.left.color = COLOR.black
                    w.color = COLOR.red
                    self.right_rotate(w)
                    w = x.parent.right
                w.color = x.parent.color
                x.parent.color = COLOR.black
                w.right.color = COLOR.black
                self.left_rotate(x.parent)
                x = self.root
            else:
                w = x.parent.left
                if w.color == COLOR.red:
                    w.color = COLOR.black
                    x.parent.color = COLOR.red
                    self.right_rotate(x.parent)
                    w = x.parent.left
                if w.right.color == COLOR.black and w.left.color == COLOR.black:
                    w.color = COLOR.red
                    x = x.parent
                elif w.left.color == COLOR.black:
                    w.right.color = COLOR.black
                    w.color = COLOR.red
                    self.left_rotate(w)
                    w = x.parent.left
                w.color = x.parent.color
                x.parent.color = COLOR.black
                w.left.color = COLOR.black
                self.right_rotate(x.parent)
                x = self.root
        x.color = COLOR.black

    def delete(self, z):
        y = z
        y_original_color = y.color
        if z.left == Nil:
            x = z.right
            self.transplant(z, z.right)
        elif z.right == Nil:
            x = z.left
            self.transplant(z, z.left)
        else:
            y = tree_successor(z.right)
            y_original_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self.transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        if y_original_color == COLOR.black:
            self.delete_fixup(x)


def bh_max(z):
    """
    求树的最大黑高
    :param z:
    :return:
    """
    height_l = 0
    height_r = 0
    if z and z != Nil:
        if z.left != Nil:
            height_l = bh_max(z.left)
        if z.right != Nil:
            height_r = bh_max(z.right)
    if z.color == COLOR.black:
        height_l += 1
        height_r += 1
    return max(height_l, height_r)


def bh_min(z):
    """
    求树的最小黑高
    :param z:
    :return:
    """
    height_l = 0
    height_r = 0
    if z and z != Nil:
        if z.left != Nil:
            height_l = bh_max(z.left)
        if z.right != Nil:
            height_r = bh_max(z.right)
    if z.color == COLOR.black:
        height_l += 1
        height_r += 1
    return min(height_l, height_r)


def rb_check(z):
    """
    检查某个结点是否是符合红黑树属性
    :param z:
    :return:
    """
    if z and z != Nil:
        # 第一条：检查结点是否有颜色
        if not z.color:
            return False
        # 第四条：检查红色结点的左右子结点是否均为黑色
        if z.color == COLOR.red:
            if z.left and z.left != Nil and z.left.color == COLOR.red:
                return False
            if z.right and z.right != Nil and z.right.color == COLOR.red:
                return False
        # 第五条：检查该节点到其所有后代叶子结点的简单路径上，是否均含有相同数目的黑色结点。
        if bh_min(z) != bh_max(z):
            return False

        return rb_check(z.left) and rb_check(z.right)
    else:
        # 如果结点为空，直接返回True
        return True


# 最小值
def tree_minimum(x):
    """
    最小值
    :param x:
    :return:
    """
    while x != Nil and x.left != Nil:
        x = x.left
    return x


# 最大值
def tree_maximum(x):
    """
    最大值
    :param x:
    :return:
    """
    while x != Nil and x.right != Nil:
        x = x.right
    return x


# 后继
def tree_successor(x):
    """
    后继
    :param x:
    :return:
    """
    if not x:
        return x
    if x.right != Nil:
        return tree_minimum(x.right)
    y = x.parent
    while y != Nil and x != y.left:
        x = y
        y = y.parent
    return y


# 前驱
def tree_predecessor(x):
    """
    前驱
    :param x:
    :return:
    """
    if not x:
        return x
    if x.left != Nil:
        return tree_maximum(x.left)
    y = x.parent
    while y != Nil and x != y.right:
        x = y
        y = y.parent
    return y
