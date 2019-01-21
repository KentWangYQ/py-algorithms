class Node(object):
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
    keys = (key for key in [6, 5, 2, 5, 7, 8])

    root = Node(key=keys.next())
    n11 = Node(key=keys.next(), parent=root, lor='left')
    n21 = Node(key=keys.next(), parent=n11, lor='left')
    n22 = Node(key=keys.next(), parent=n11, lor='right')
    n12 = Node(key=keys.next(), parent=root, lor='right')
    n23 = Node(key=keys.next(), parent=n12, lor='right')

    return root


pst_demo = create()


def inorder_tree_walk_recursive(x):
    if x:
        inorder_tree_walk_recursive(x.left)
        print x.key
        inorder_tree_walk_recursive(x.right)


def inorder_tree_walk_stack(x):
    stack = [x]
    while len(stack) > 0:
        while stack[-1].left:
            stack.append(stack[-1].left)

        while len(stack) > 0:
            temp = stack.pop()  # type: Node
            print temp.key
            if temp.right:
                stack.append(temp.right)
                break


def test():
    inorder_tree_walk_recursive(pst_demo)
    print '----------------'
    inorder_tree_walk_stack(pst_demo)


test()
