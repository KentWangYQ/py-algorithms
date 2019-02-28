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
    # 遍历已排序链表，反写会原始数组
    for i in range(len(a)):
        a[i] = sl[c].rc
        c = sl[c].next


# endregion

def _merge(a, p, q, r, reverse=False):
    sentry = float('-inf') if reverse else float('inf')
    l_a = [v for i, v in enumerate(a) if p <= i <= q]
    l_a.append(sentry)

    r_a = [v for i, v in enumerate(a) if q < i <= r]
    r_a.append(sentry)

    i, j, k = 0, 0, p
    while l_a[i] is not sentry or r_a[j] is not sentry:
        if l_a[i] > r_a[j] if reverse else l_a[i] < r_a[j]:
            a[k] = l_a[i]
            i += 1
        else:
            a[k] = r_a[j]
            j += 1
        k += 1


def _merge_sort(a, p, r, reverse=False):
    if p < r:
        q = (r + p) // 2
        _merge_sort(a, p, q, reverse=reverse)
        _merge_sort(a, q + 1, r, reverse=reverse)
        _merge(a, p, q, r, reverse=reverse)


def merge_sort(a, reverse=False):
    _merge_sort(a, 0, len(a) - 1, reverse)


def heap_sort(a, reverse=False):
    heap = (MinHeap if reverse else MaxHeap)(a)

    for i in range(heap.heap_size - 1, 0, -1):
        heap.A[0], heap.A[i] = heap.A[i], heap.A[0]
        heap.heap_size -= 1
        heap.heapify(0)


def _partition(a, p, r, reverse=False):
    i = p - 1
    for j in range(p, r):
        compare = (a[j] > a[r]) if reverse else (a[j] < a[r])
        if compare:
            i += 1
            a[i], a[j] = a[j], a[i]
    a[i + 1], a[r] = a[r], a[i + 1]
    return i + 1


def _randomized_partition(a, p, r, reverse=False):
    k = random.randint(p, r)
    a[k], a[r] = a[r], a[k]
    return _partition(a, p, r, reverse)


def _quick_sort(a, p, r, reverse=False, randomized_partition=False):
    if p < r:
        q = _randomized_partition(a, p, r, reverse) if randomized_partition else _partition(a, p, r, reverse)
        _quick_sort(a, p, q - 1, reverse)
        _quick_sort(a, q + 1, r, reverse)


def quick_sort(a, reverse=False, randomized_partition=False):
    _quick_sort(a, 0, len(a) - 1, reverse, randomized_partition)
