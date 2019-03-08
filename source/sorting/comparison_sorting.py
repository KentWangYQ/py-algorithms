# -*- coding: utf-8 -*-
import random

from source.tree.heap import MinHeap, MaxHeap


# region INSERTION SORT

# 直接插入排序
def straight_insertion_sort(a, reverse=False):
    """
    直接插入排序
    基本操作：将一个记录插入到已排好序的有序表中，从而得到一个新的，记录数增加1的有序表。
    :param a:
    :param reverse:
    :return:
    """
    # 从无序表的第二条记录开始
    for i in range(1, len(a)):
        j = i
        # 将索引为i的元素插入到前面的有序表的适当位置
        while j > 0 and (a[j] > a[j - 1] if reverse else a[j] < a[j - 1]):
            # 通过依次交换的方式移动记录
            a[j - 1], a[j] = a[j], a[j - 1]
            # 索引指针前移
            j -= 1


# 折半插入排序
def binary_insertion_sort(a, reverse=False):
    """
    折半插入排序
    基本操作：在直接插入排序的基础上改进，基本操作与直接插入排序一致，使用"折半查找"来确定插入位置
    :param a:
    :param reverse:
    :return:
    """
    # 从无序表的第二条记录开始
    for i in range(1, len(a)):
        # 折半查找插入位置
        low = 0
        high = i - 1
        while low <= high:
            m = (low + high) // 2  # 折半
            if a[i] >= a[m] if reverse else a[i] <= a[m]:
                if a[i] == a[m]:
                    high = m
                    break
                high = m - 1
            else:
                low = m + 1

        v = a[i]
        # 记录依次后移，空出目标位置
        for j in range(i - 1, high, -1):
            a[j + 1], a[j] = a[j], a[j + 1]
        # 目标值插入目标位置
        a[high + 1] = v


# 2路插入排序
def two_way_insertion_sort(a, reverse=False):
    """
    2路插入排序
    基本操作：在“折半插入排序算法”的基础上进行改进，目的是减少排序过程中记录移动的次数。
    使用一个长度为n的循环表作为辅助空间，将原表中的记录依次的插入循环表。并使用指针first和final指示有序序列的最小和最大值。
    对于记录i：
        1. 如果小于first：直接插入到有序序列之前；
        2. 如果大于final：直接追加到有序序列之后；
        3. 如果介于两者之间：查找位置并插入(可用高效查找算法提高效率)。
    :param a:
    :param reverse:
    :return:
    """
    n = len(a)
    deque = [0] * n
    deque[0] = a[0]
    first, final = 0, 0

    for i, v in enumerate(a):
        if i > 0:
            if v < deque[first]:
                # 情况1：插入到有序序列之前
                first = (first - 1 + n) % n
                deque[first] = v
            elif v > deque[final]:
                # 情况2：追加到有序序列之后
                final = (final + 1 + n) % n
                deque[final] = v
            else:
                # 情况3：查找并插入
                # 为了简化代码，此处使用了直接插入；可以使用高效查找算法提高效率，如折半查找
                i = first
                while deque[i] < v:
                    deque[(i - 1 + n) % n] = deque[i]
                    i = (i + 1 + n) % n
                deque[i - 1] = v
                first = (first - 1 + n) % n

    # 将循环表中的记录还原到原表
    for i in range(n):
        if reverse:
            a[n - 1 - i] = deque[(first + i + n) % n]
        else:
            a[i] = deque[(first + i + n) % n]


# 链表结点
class SLNode(object):
    """
    链表结点，用于表插入排序
    """

    def __init__(self, rc, _next):
        self.rc = rc  # 记录值
        self.next = _next  # 链接指针


# 重排链表
def _arrange(sl):
    """
    重排链表
    表插入排序的辅助方法
    顺序遍历有序链表，将链表中的第i个结点移动至数组的第i个分量中。
    链表方便移动，但是无法实现高效查找；所以对链表进行重排，最终变成有序数据，进而支持高效查找。
    :param sl:
    :return:
    """
    p = sl[0].next  # 当前操作的结点
    for i in range(1, len(sl) - 1):
        q = sl[p].next  # 当前结点的下一个结点
        '''
        使用p的next来暂存交换后的下一个结点的实际位置
        此处比较绕，当前结点p在与数组索引为i的结点k进行对调之后，k失去了原来的位置。
        链表中k之前的结点k'的next依然是指向i，但这时候k'通过next已经无法找到k了，因为i位置现在存储的是结点p。
        同时p因为已经被放置在了有序数组中的恰当位置，其next字段已经无用，所以我们使用p的next字段来指示当前结点k的实际位置。
        当k'通过next访问下一个结点时，实际访问到的是结点p，我们判断结点p已经处在数组中的有序区域，因此继续访问next，
        直到next不在有序数组范围，即为原链表实际的next位置。
        '''
        # 暂存k的位置
        sl[p].next = p
        # 结点交换
        sl[i], sl[p] = sl[p], sl[i]
        # 循环获取next的实际位置
        while q <= i:
            q = sl[q].next
        # 指针后移
        p = q


# 表插入排序
def list_insertion_sort(a, reverse=False):
    """
    表插入排序
    插入排序的改进。普通插入排序使用数组来存储数据，无法避免移动记录。表插入排序改用链表来存储数据，完全避免的记录移动。
    :param a:
    :param reverse:
    :return:
    """
    # 使用数组+链表结点来模拟链表
    sl = [SLNode(None, None) for _ in range(len(a) + 1)]

    # 首结点作为哨兵
    sl[0].rc = float('-inf' if reverse else 'inf')
    sl[0].next = 0

    # 遍历原始数组，依次将记录插入链表
    for i, v in enumerate(a):
        i += 1
        curr = 0
        # 遍历链表，找到合适的插入位置
        while v < sl[sl[curr].next].rc if reverse else v > sl[sl[curr].next].rc:
            curr = sl[curr].next

        # 向已排序链表中插入新记录
        sl[i].rc = v
        sl[i].next = sl[curr].next
        sl[curr].next = i

    c = sl[0].next
    # 遍历已排序链表，反写灰原始数组
    for i in range(len(a)):
        a[i] = sl[c].rc
        c = sl[c].next


def _shell_insert(a, dk, reverse=False):
    """
    希尔插入
    希尔排序的辅助方法，完成一趟排序操作
    对每个分组内的记录，分别进行直接插入排序
    :param a:
    :param dk:
    :param reverse:
    :return:
    """
    for i in range(dk, len(a)):
        j = i - dk
        while j >= 0 and (a[i] > a[j] if reverse else a[i] < a[j]):
            a[i], a[j] = a[j], a[i]
            i, j = j, j - dk


# 希尔排序
def shell_sort(a, dlta, reverse=False):
    """
    希尔排序(Shell Sort)
    又称“缩小增量排序(Diminishing Increment Sort)”
    直接插入排序在待排序列基本有序或记录较少时，效率非常高。希尔排序就是借助这个特点，
    将待排序列分割成若干个子序列分别进行插入排序，待整个序列基本有序时，再对全体记录做一次直接插入排序。
    通过多次由大到小的分割，逐趟进行希尔插入操作，直到间隔为1，也就是全体排序。
    分割的方式为：增量为k，间隔为k的记录为一组
    :param a:
    :param dlta: 增加序列
    :param reverse:
    :return:
    """
    # 根据增量序列逐趟进行希尔插入操作
    for dk in dlta:
        _shell_insert(a, dk, reverse)


# endregion


# region QUICK SORT

# 冒泡排序
def bubble_sort(a, reverse=False):
    """
    冒泡排序
    一趟的操作：
    升序为例，按顺序比较相邻的两条记录，如果两者不是升序排列，则交换两记录。
    一趟结束时，待排序列中最大的记录会沉底，下一趟则从待排序列中排除掉该记录。
    直到待排序列只剩一条记录时，排序完成。
    :param a:
    :param reverse:
    :return:
    """
    n = len(a)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if (a[j] < a[j + 1]) if reverse else (a[j] > a[j + 1]):
                a[j], a[j + 1] = a[j + 1], a[j]


# 分割待排记录
def _partition(a, p, r, reverse=False):
    """
    分割待排记录
    将索引从p到r的记录，已a[r]为支点分割为独立的两部分，其中一部分的记录均小于另一部分。
    :param a:
    :param p:
    :param r:
    :param reverse:
    :return:
    """
    i = p - 1  # 两部分支点，第一部分的最后一条记录
    # 遍历待排记录，并将记录移动到所属的部分
    for j in range(p, r):
        compare = (a[j] > a[r]) if reverse else (a[j] < a[r])
        if compare:
            # 需要移动
            i += 1  # 支点后移
            a[i], a[j] = a[j], a[i]  # 移动记录
    a[i + 1], a[r] = a[r], a[i + 1]  # 将最后一条记录(索引为r)与第二部分的第一个元素交换，r正式称为支点
    return i + 1  # 返回支点索引


# 随机分割
def _randomized_partition(a, p, r, reverse=False):
    """
    随机分割
    普通分割策略使用待排记录中的最后一条记录作为支点，如果分割后的两部分严重不平衡，会造成算法性能下降。
    所以该方法使用随机选取支点记录的策略，使两部分平衡的概率稳定，进而使整个排序算法的性能稳定。
    :param a:
    :param p:
    :param r:
    :param reverse:
    :return:
    """
    k = random.randint(p, r)  # 随机选取支点记录
    a[k], a[r] = a[r], a[k]
    return _partition(a, p, r, reverse)


# 快速排序
def _quick_sort(a, p, r, reverse=False, randomized_partition=False):
    """
    快速排序
    计算支点索引，并递归排序前后两部分
    :param a:
    :param p:
    :param r:
    :param reverse:
    :param randomized_partition:
    :return:
    """
    if p < r:
        # 待排记录中有多于一条记录

        # 获取支点索引
        q = _randomized_partition(a, p, r, reverse) if randomized_partition else _partition(a, p, r, reverse)

        # 递归排序前后两部分
        _quick_sort(a, p, q - 1, reverse)
        _quick_sort(a, q + 1, r, reverse)


# 快速排序封装方法
def quick_sort(a, reverse=False, randomized_partition=False):
    """
    快速排序封装方法
    :param a:
    :param reverse:
    :param randomized_partition:
    :return:
    """
    _quick_sort(a, 0, len(a) - 1, reverse, randomized_partition)


# endregion


# region SELECTION SORT

# 简单选择排序
def simple_selection_sort(a, reverse=False):
    """
    简单选择排序
    实现最简单的选择排序
    基本操作：每次选出待排序类中最小(或最大)的记录，移动至有序序列中；循环多趟直至最后一条记录。
    :param a:
    :param reverse:
    :return:
    """
    n = len(a)
    for i in range(n - 1):
        k = i
        for j in range(i + 1, n):
            if (a[k] < a[j]) if reverse else (a[k] > a[j]):
                k = j
        if k != i:
            a[k], a[i] = a[i], a[k]


# 树形选择排序
def tree_selection_sort(a):
    """
    树形选择排序
    因为过程类似锦标赛制，又称锦标赛排序(Tournament Sort)。

    是对“简单选择排序”的改进。简单选择排序主要操作是记录的对比，如果能减少对比，则可以提高效率

    树形选择排序基本操作：对n个记录进行两两对比，然后其中1/2较小的记录再进行两两对比，如此反复，直至选出最小记录。
    过程可用一棵完全二叉树表示。n条记录依次放入叶子结点，按如上规则生成二叉树。
    获取第二小的记录：已知树根结点记录为最小记录，找到最小记录在叶节点中的位置，将其置为无穷大；
    然后沿该结点到根结点的路径重新生成二叉树，则生成完毕之后，树根为第二小的记录；后续以此类推。

    该排序方法有辅助空间较多和最大值进行多余比较等缺点，另一种选择排序：堆排序弥补了这些缺点。
    所以树形选择排序只是一种过度，实现比较复杂，应用很少。
    :param a:
    :return:
    """

    # 树结点
    class Node(object):
        def __init__(self, key, parent=None, left=None, right=None):
            self.key = key
            self.parent = parent
            self.left = left
            self.right = right

    # 哨兵值
    sentry = float('inf')

    # 根据待排序列生成二叉树
    def generate_tree():
        l1, l2 = [], []
        # 生成叶子结点
        for key in a:
            l1.append(Node(key))

        # 向上逐层生成，直至只剩一个结点，即为根结点
        while len(l1) > 1:
            # 如果结点数为奇数，追加一个凑为偶数个，方便二叉树生成
            if len(l1) & 1:
                l1.append(Node(sentry))

            # 步进为2，两两对比选出父结点
            for i in range(0, len(l1), 2):
                node = Node(key=l1[i].key if (l1[i].key < l1[i + 1].key) else l1[i + 1].key, left=l1[i],
                            right=l1[i + 1])
                l1[i].parent = node
                l1[i + 1].parent = node
                l2.append(node)
            l1, l2 = l2, []
        # 最后一个结点即为根结点
        return l1.pop()

    # 迭代获取最小值
    def get_extremum_from_tree():
        node = tree_root
        while node.key != sentry:
            # 使用生成器函数来进行迭代
            # 返回最小值后，将最小结点记录变为无穷大，重新生成二叉树
            yield node.key
            # 寻找最小记录所在的叶子结点
            while node and node.left:
                node = node.left if node.key == node.left.key else node.right
            # 最小记录标记为无穷大
            node.key = sentry

            while node and node.parent:
                node = node.parent
                node.key = node.left.key if node.left.key < node.right.key else node.right.key
        return

    # 生成二叉树
    tree_root = generate_tree()
    # 迭代生成有序序列，并返回
    return [v for v in get_extremum_from_tree()]


# 堆排序
def heap_sort(a, reverse=False):
    """
    堆排序
    借助最大堆(或最小堆)的性质实现排序，是对“树形选择排序”的改进
    基本操作：从堆的根结点获取最小记录，放入有序序列，剩余的序列重新建堆。以此类推，直至所有记录有序。
    :param a:
    :param reverse:
    :return:
    """
    # 使用待排序列初始化最大堆(最小堆)
    heap = (MinHeap if reverse else MaxHeap)(a)

    for i in range(heap.heap_size - 1, 0, -1):
        # 最小记录移动至序列尾部形成有序序列
        heap.A[0], heap.A[i] = heap.A[i], heap.A[0]
        # 堆元素减少
        heap.heap_size -= 1
        # 重新建堆
        heap.heapify(0)


# endregion


# region MERGE SORT

# 合并有序序列
def _merge(a, p, q, r, reverse=False):
    """
    合并有序序列
    将两个有序序列合并为一个新的有序序列
    “归并排序”辅助方法
    依次对比前后两部分的记录，按顺序合并进原序列
    :param a:
    :param p:
    :param q:
    :param r:
    :param reverse:
    :return:
    """
    # 哨兵
    sentry = float('-inf') if reverse else float('inf')

    # 获取前半部分有序序列
    l_a = [v for i, v in enumerate(a) if p <= i <= q]
    # 追加哨兵
    l_a.append(sentry)

    # 获取后半部分有序序列
    r_a = [v for i, v in enumerate(a) if q < i <= r]
    # 追加哨兵
    r_a.append(sentry)

    # 遍历l_a和l_b，对比两个序列中的记录，按顺序回写如原序列
    i, j, k = 0, 0, p
    while l_a[i] is not sentry or r_a[j] is not sentry:
        if l_a[i] > r_a[j] if reverse else l_a[i] < r_a[j]:
            a[k] = l_a[i]
            i += 1
        else:
            a[k] = r_a[j]
            j += 1
        k += 1


# 归并排序
def _merge_sort(a, p, r, reverse=False):
    """
    归并排序
    主要思想：将两个或两个以上的有序序列组合成一个新的有序序列
    该方法实现的是2路归并排序。主要操作是，递归的将待排序类均分为两部分，
    直到细分到每部分只有一条记录(一条记录天然有序)，然后逐层合并，最终得到有序序列。
    :param a:
    :param p:
    :param r:
    :param reverse:
    :return:
    """
    if p < r:
        # 均分待排序列
        q = (r + p) // 2

        # 递归排序前后两部分
        _merge_sort(a, p, q, reverse=reverse)
        _merge_sort(a, q + 1, r, reverse=reverse)

        # 前后两部分分别有序后，合并之
        _merge(a, p, q, r, reverse=reverse)


# 归并排序封装方法
def merge_sort(a, reverse=False):
    """
    归并排序封装方法
    :param a:
    :param reverse:
    :return:
    """
    _merge_sort(a, 0, len(a) - 1, reverse)
# endregion
