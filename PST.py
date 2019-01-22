# coding=utf-8


class Node(object):
    """
    PST Node 二叉搜索树结点
    """
    left = None
    right = None
    parent = None

    def __init__(self, key, data=None, parent=None, lor='left'):
        self.key = key
        self.data = data
        if parent:
            self.parent = parent

            if lor == 'left':
                self.parent.left = self
            else:
                self.parent.right = self


def create():
    """
    生成demo tree
         7
        / \
       5   8
      / \   \
     2  6    9
    :return:
    """
    keys = (key for key in [7, 5, 2, 6, 8, 9])

    root = Node(key=next(keys))
    n11 = Node(key=next(keys), parent=root, lor='left')
    n21 = Node(key=next(keys), parent=n11, lor='left')
    n22 = Node(key=next(keys), parent=n11, lor='right')
    n12 = Node(key=next(keys), parent=root, lor='right')
    n23 = Node(key=next(keys), parent=n12, lor='right')

    return root


pst_demo = create()


def inorder_tree_walk_recursive(x):
    """
    中序遍历(递归)
    :param x:
    :return:
    """
    if x:
        inorder_tree_walk_recursive(x.left)
        print(x.key)
        inorder_tree_walk_recursive(x.right)


def inorder_tree_walk_stack(x):
    """
    中序遍历(堆栈)
    :param x:
    :return:
    """
    stack = [x]
    while len(stack) > 0:
        while stack[-1].left:
            stack.append(stack[-1].left)

        while len(stack) > 0:
            temp = stack.pop()  # type: Node
            print(temp.key)
            if temp.right:
                stack.append(temp.right)
                break


def inorder_tree_walk_pointer(x):
    """
    中序遍历(非递归，非堆栈)
    :param x:
    :return:
    """
    temp = None
    while x:
        if temp != x.left:  # 如果不是左回溯，向左钻取
            while x.left:
                x = x.left
        # 得到子树的最左侧结点，打印
        print(x.key)

        # 如果存在右子结点，处理右子树
        if x.right:
            x = x.right
        else:  # 如果没有右子树，回溯
            while True:
                # 如果是右回溯，一直向上回溯，直到不是右回溯或到根结点
                temp = x
                x = x.parent
                if not x or temp != x.right:
                    break


def test_tree_walk():
    inorder_tree_walk_recursive(pst_demo)
    print('----------------')
    inorder_tree_walk_stack(pst_demo)
    print('----------------')
    inorder_tree_walk_pointer(pst_demo)


def tree_search(x, key):
    """
    二叉搜索树查询(递归)
    :param x:
    :param key:
    :return:
    """
    if not x or x.key == key:
        return x

    if key < x.key:
        return tree_search(x.left, key)
    else:
        return tree_search(x.right, key)


def iterative_tree_search(x, key):
    """
    二叉搜索树查询(迭代)
    :param x:
    :param key:
    :return:
    """
    while x and x.key != key:
        if key < x.key:
            x = x.left
        else:
            x = x.right

    return x


def tree_minimum(x):
    """
    二叉搜索树最小值
    :param x:
    :return:
    """
    while x and x.left:
        x = x.left
    return x


def tree_maximum(x):
    """
    二叉搜索树最大值
    :param x:
    :return:
    """
    while x and x.right:
        x = x.right
    return x


def tree_successor(x):
    """
    二叉搜索树后继
    :param x:
    :return:
    """
    if not x:
        return x
    if x.right:
        return tree_minimum(x)
    y = x.parent
    while y and x != y.left:
        x = y
        y = y.parent
    return y


def tree_predecessor(x):
    """
    二叉搜索树前驱
    :param x:
    :return:
    """
    if not x:
        return x
    if x.left:
        return tree_maximum(x.left)
    y = x.parent
    while y and x != y.right:
        x = y
        y = y.parent
    return y


def test_tree_search():
    """
    tree search test
    :return:
    """
    key = 8
    # result = tree_search(pst_demo, key)
    result = iterative_tree_search(pst_demo, key)
    if result:
        print('result key: %s' % result.key)
    else:
        print('result key: %s NOT FOUND' % key)

    minimum = tree_minimum(pst_demo)
    if minimum:
        print('minimum: %s' % minimum.key)
    else:
        print('Tree is None')

    maximum = tree_maximum(pst_demo)
    if maximum:
        print('maximum: %s' % maximum.key)
    else:
        print('Tree is None')

    successor = tree_successor(pst_demo.left.right)
    if successor:
        print('Node 6\'s successor is: %s' % successor.key)
    else:
        print('Tree is None')

    predecessor = tree_predecessor(pst_demo.left.right)
    if predecessor:
        print('Node 6\'s predecessor is: %s' % predecessor.key)
    else:
        print('Tree is None')


test_tree_search()
