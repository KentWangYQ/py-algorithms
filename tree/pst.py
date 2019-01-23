# coding=utf-8


class Node(object):
    """
    PST Node 结点
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


class Tree(object):
    def __init__(self, root=None):
        self.root = root


# 插入结点
def tree_insert(t, z):
    """
    插入结点
    :param t:
    :param z:
    :return:
    """
    assert t, 't can not be None'
    if not t.root:
        t.root = z
        return t

    x = t.root
    y = None
    while x:
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
    return t


# 生成demo tree
def create_tree(keys):
    """
    生成demo tree
         7
        / \
       5   8
      / \   \
     2  6    9
    :return:
    """
    tree = Tree()
    for key in keys:
        tree_insert(tree, Node(key=key))

    # keys = (key for key in keys)
    #
    # root = Node(key=next(keys))
    # n11 = Node(key=next(keys), parent=root, lor='left')
    # n21 = Node(key=next(keys), parent=n11, lor='left')
    # n22 = Node(key=next(keys), parent=n11, lor='right')
    # n12 = Node(key=next(keys), parent=root, lor='right')
    # n23 = Node(key=next(keys), parent=n12, lor='right')

    return tree


# 中序遍历(递归)
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


# 中序遍历(堆栈)
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


# 中序遍历(非递归，非堆栈)
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


# 查询(递归)
def tree_search(x, key):
    """
    查询(递归)
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


# 查询(迭代)
def iterative_tree_search(x, key):
    """
    查询(迭代)
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


# 最小值
def tree_minimum(x):
    """
    最小值
    :param x:
    :return:
    """
    while x and x.left:
        x = x.left
    return x


# 最大值
def tree_maximum(x):
    """
    最大值
    :param x:
    :return:
    """
    while x and x.right:
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
    if x.right:
        return tree_minimum(x.right)
    y = x.parent
    while y and x != y.left:
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
    if x.left:
        return tree_maximum(x.left)
    y = x.parent
    while y and x != y.right:
        x = y
        y = y.parent
    return y


# 子树替换
def transplant(t, u, v):
    """
    子树替换
    :param t:
    :param u:
    :param v:
    :return:
    """
    assert u, 'u can not be None'

    if not u.parent:
        t.root = v
    elif u == u.parent.left:
        u.parent.left = v
    else:
        u.parent.right = v

    if v:
        v.parent = u.parent

    return t


#  删除结点
def tree_delete(t, z):
    """
    删除结点
    三种情况：
        1. 要删除的结点是叶子结点z，直接删除。
        2. 要删除的结点是非叶子结点z，且只有一个子结点y，使用其左或右结点y替代该结点z。
        3. 要删除的结点是非叶子结点z，且有两个子节点，这种情况比较复杂。
            1. 获取z的后继y，y位于z的右子树中，并且没有左子结点。
            2. y的右子结点替换y
            3. y替换z
    :param t:
    :param z:
    :return:
    """
    if not z.left:
        transplant(t, z, z.right)
    elif not z.right:
        transplant(t, z, z.left)
    else:
        y = tree_successor(z)
        if y != z.right:
            transplant(t, y, y.right)
            y.right = z.right
            y.right.parent = y

        transplant(t, z, y)
        y.left = z.left
        y.left.parent = y
    if z == t.root:
        t.root = y
    return t
