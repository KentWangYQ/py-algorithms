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
        self.left = Nil
        self.right = Nil


class RBTree(BSTree):
    """
    红黑树
    继承自 BSTree
    """

    def __init__(self, root=None, keys=None):
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
        if not self.root:
            self.root = z
        else:
            x = self.root
            y = None
            while x and x != Nil:
                y = x
                if z.key < x.key:
                    x = x.left
                else:
                    x = x.right

            if z.key < y.key:
                y.left = z
            else:
                y.right = z

            z.parent = y

        self.fixup(z)

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

    def fixup(self, z):
        """
        修正红黑树
        添加或删除结点后，会造成树不再满足红黑树的性质，通过该方法来修正新树为红黑树
        :param z:
        :return:
        """
        while z.parent and z.parent.parent and z.parent.color == COLOR.red:  # 父结点为红色
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


def black_height_max(z):
    """
    求树的最大黑高
    :param z:
    :return:
    """
    height_l = 0
    height_r = 0
    if z:
        if z.left:
            height_l = black_height_max(z.left)
        if z.right:
            height_r = black_height_max(z.right)
    if z.color == COLOR.black:
        height_l += 1
        height_r += 1
    return max(height_l, height_r)


def black_height_min(z):
    """
    求树的最小黑高
    :param z:
    :return:
    """
    height_l = 0
    height_r = 0
    if z:
        if z.left:
            height_l = black_height_max(z.left)
        if z.right:
            height_r = black_height_max(z.right)
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
    if z:
        # 第一条：检查结点是否有颜色
        if not z.color:
            return False
        # 第四条：检查红色结点的左右子结点是否均为黑色
        if z.color == COLOR.red:
            if z.left and z.left.color == COLOR.red:
                return False
            if z.right and z.right.color == COLOR.red:
                return False
        # 第五条：检查该节点到其所有后代叶子结点的简单路径上，是否均含有相同数目的黑色结点。
        if black_height_min(z) != black_height_max(z):
            return False

        return rb_check(z.left) and rb_check(z.right)
    else:
        # 如果结点为空，直接返回True
        return True
