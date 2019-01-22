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

    root = Node(key=keys.__next__())
    n11 = Node(key=keys.__next__(), parent=root, lor='left')
    n21 = Node(key=keys.__next__(), parent=n11, lor='left')
    n22 = Node(key=keys.__next__(), parent=n11, lor='right')
    n12 = Node(key=keys.__next__(), parent=root, lor='right')
    n23 = Node(key=keys.__next__(), parent=n12, lor='right')

    return root


pst_demo = create()


def inorder_tree_walk_recursive(x):
    """
    中序遍历，使用递归
    :param x:
    :return:
    """
    if x:
        inorder_tree_walk_recursive(x.left)
        print(x.key)
        inorder_tree_walk_recursive(x.right)


def inorder_tree_walk_stack(x):
    """
    中序遍历，使用堆栈
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
    中序遍历，不使用递归，不使用堆栈
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


def test():
    inorder_tree_walk_recursive(pst_demo)
    print('----------------')
    inorder_tree_walk_stack(pst_demo)
    print('----------------')
    inorder_tree_walk_pointer(pst_demo)


test()
