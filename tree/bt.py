# coding=utf-8


class BNode(object):
    """
    B-Tree 结点
    """
    keys = []  # 键
    c = []  # 子结点
    n = 0  # 关键字个数
    leaf = True  # 是否为叶子结点

    def __init__(self, t=5):
        self.keys = [None] * (2 * t - 1)
        self.c = [None] * (2 * t)


class BTree(object):
    """
    B-Tree
    """

    def __init__(self, root=None, t=2):
        self.root = root  # 根结点
        self.t = t  # 最小度数

    def create(self):
        """
        创建B-Tree
        :return:
        """
        x = ALLOCATE_NODE(t=self.t)
        DISK_WRITE(x)
        self.root = x

    def split_node(self, x, i):
        """
        拆分满结点
        :param x:
        :param i:
        :return:
        """
        z = ALLOCATE_NODE(t=self.t)  # type:BNode # 分配新的结点
        y = x.c[i]  # type:BNode # 待分割的结点
        z.leaf = y.leaf  # 新结点与待分割结点处在同一层级
        z.n = self.t - 1  # 新结点其实容量t-1

        # 将结点y中的后半部分key转移到z中
        for j in range(self.t - 1):
            z.keys[j] = y.keys[j + self.t]
            y.keys[j + self.t] = None

        # 如果y不是叶子结点，将y的后半部分子结点转移到z中
        if not y.leaf:
            for j in range(self.t):
                z.c[j] = y.c[j + self.t]
                y.c[j + self.t] = None

        y.n = self.t - 1  # y键减少，修正计数器。注意此时y.keys实际有t个key，第t个尚未移除

        # 父结点x的子结点列表空出i位置，插入z
        for j in range(x.n, i, -1):
            x.c[j + 1] = x.c[j]
        x.c[i + 1] = z

        # 父结点x的键列表空出i位置，插入y的中间 键
        for j in range(x.n - 1, i - 1, -1):
            x.keys[j + 1] = x.keys[j]
        x.keys[i] = y.keys[self.t - 1]
        y.keys[self.t - 1] = None

        x.n += 1  # 修正x键计数器

        # 修改过的结点写入磁盘
        DISK_WRITE(x)
        DISK_WRITE(y)
        DISK_WRITE(z)

    def insert_nonfull(self, x, k):
        """
        插入新结点(非满结点)
        :param x:
        :param k:
        :return:
        """
        i = x.n - 1
        # 如果是叶子结点，直接在适当位置插入新键
        if x.leaf:
            while i >= 0 and k < x.keys[i]:
                x.keys[i + 1] = x.keys[i]
                i -= 1
            x.keys[i + 1] = k
            x.n += 1
            DISK_WRITE(x)
        else:
            # 不是叶子结点，向下逐层迭代

            # 找到需要键区间。
            while i >= 0 and k < x.keys[i]:
                i -= 1
            i += 1
            DISK_READ(x.c[i])
            # 如果子结点为满结点，进行拆分
            if x.c[i].n >= 2 * self.t - 1:
                self.split_node(x, i)
                if k > x.keys[i]:
                    i += 1

            # 向下迭代
            self.insert_nonfull(x.c[i], k)

    def insert(self, k):
        """
        插入新结点
        :param k:
        :return:
        """
        r = self.root
        if r.n >= 2 * self.t - 1:
            # 如果根结点已满，先拆分，再插入
            s = ALLOCATE_NODE(t=self.t)  # type: BNode
            self.root = s
            s.c[0] = r
            s.leaf = False
            self.split_node(s, 0)
            self.insert_nonfull(s, k)
        else:
            # 直接按照非满规则插入
            self.insert_nonfull(r, k)

    def search(self, x, k):
        """
        键搜索
        :param x:
        :param k:
        :return:
        """
        i = 0
        while i < x.n and k > x.keys[i]:
            i += 1
        if k == x.keys[i]:
            return x, i

        if x.leaf:
            return None

        return self.search(x.c[i], k)


def ALLOCATE_NODE(t=5):
    """
    创建并初始化一个B-Tree结点
    :param t:
    :return:
    """
    return BNode(t)


def DISK_READ(x):
    """
    模拟磁盘读操作
    :param x:
    :return:
    """
    # print('Read "x" from disk!')
    pass


def DISK_WRITE(x):
    """
    模拟磁盘写操作
    :param x:
    :return:
    """
    # print('Write "x" to disk!')
    pass
