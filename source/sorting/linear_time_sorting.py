# -*- coding: utf-8 -*-

from source.sorting import comparison_sorting


def counting_sort(a, k, reverse=False):
    """
    计数排序
    基本思想：对每一条记录，计算小于这条记录的记录个数。利用这一信息，就可以直接确定该记录的位置。
    当有几条记录相同时，则需要调整一下位置。
    记录值分布在0-k之间，建立C[0...k]，根据记录值找到在C中的位置，该位置计数器+1。
    数组C中某个位置Ci，C[0...i-1]的所有值相加，即为小于i的记录的个数。依次计算C[1...k]的值，即C[i]=C[i]+C[i-1]。
    根据C中数据重新确定待排序列中记录的位置。

    :param a:
    :param k:
    :param reverse:
    :return:
    """
    b = [0] * len(a)  # 有序序列输出辅助
    c = [0] * (k + 1)  # 计数辅助
    # 计数
    for v in a:
        c[v] += 1

    if reverse:
        # 计算比记录i大的记录的个数
        for i in range(len(c) - 2, -1, -1):
            c[i] += c[i + 1]
    else:
        # 计算比记录i小的记录的个数
        for i in range(1, len(c)):
            c[i] += c[i - 1]

    for v in a:
        # 根据C数据，定位记录到输出序列
        b[c[v] - 1] = v
        # 如果有多条相同的记录，调整位置
        c[v] -= 1

    return b


def radix_sort(a, d, reverse=False):
    """
    基数排序
    基数排序实际是一种多关键字排序。使用稳定排序依次对关键字进行稳定排序，最终得到整体有序序列。
    根据使用关键字的顺序，分为“最高位优先(Most Significant Digit first, MSD)”和“最地位优先(Least Significant Digit first, LSD)”。使用时，两者稍有不同。
    本方法实现对数字的基数排序，数字的每一位作为一个关键字，使用LSD。对单个关键字使用“计数排序算法”进行排序。
    :param a:
    :param d:
    :param reverse:
    :return:
    """

    # 计数排序，单关键字排序算法，具体参见“计数排序算法”
    def _counting_sort(_a, _digit, _k):
        _b = [0] * len(_a)
        _c = [0] * _k

        for v in _digit:
            _c[v] += 1

        if reverse:
            for _i in range(len(_c) - 2, -1, -1):
                _c[_i] = _c[_i] + _c[_i + 1]
        else:
            for _i in range(1, len(_c)):
                _c[_i] = _c[_i] + _c[_i - 1]

        for _i in range(len(_a) - 1, -1, -1):
            _b[_c[_digit[_i]] - 1] = _a[_i]
            _c[_digit[_i]] -= 1

        return _b

    k = 10
    # 每一位作为一个关键字进行多轮排序
    for i in range(d - 1, -1, -1):
        # 由低到高对数字的每一位进行稳定排序
        # 此处使用计数排序，因为每位只有0-9是个可选项，非常适合进行计数排序
        # 将待排记录统一成d为，不足d位的，前面补0
        a = _counting_sort(a, [int(str(v).zfill(d)[i]) for v in a], k)

    return a


def link_radix_sort(a, d, reverse=False):
    """
    链式基数排序
    基数排序算法的改进，普通基数排序算法需要大量的辅助空间n+RADIX，链式基数排序解决了这个问题。
    通过引入链表结构，可以在原址改变记录的相对位置关系，所以仅需要2×RADIX个辅助空间即可。
    本例中对数字进行排序，则RADIX=10
    :param a:
    :param d:
    :return:
    """

    # 结点
    class Node(object):
        def __init__(self, keys, _next):
            self.keys = keys
            self.next = _next

    _SENTRY = Node(keys=[], _next=None)  # 哨兵
    _RADIX = 10  # 基数数域
    f, e = None, None  # 基数中的头尾数组
    r = _SENTRY  # 待排序列头

    def distribute(ki):
        """
        分配操作，将记录根据指定的基数，分配到基数数组中
        :param ki:
        :return:
        """
        cn = r.next
        while cn:
            i = (_RADIX - cn.keys[ki] - 1) if reverse else cn.keys[ki]
            if not f[i]:
                # 该组中出现的第一条记录，存入头数组
                f[i] = cn
            else:
                # 否则，追加在该组最后一条记录之后
                e[i].next = cn
            # 尾数组之前后移
            e[i] = cn
            # 待排记录链表指针后移
            cn = cn.next

    def collect():
        """
        收集操作，将基数数组中的记录，依照顺序收尾相连，形成中间待排序列。
        :return:
        """
        c = r
        # 遍历基数数组
        for i in range(_RADIX):
            if f[i]:
                # 如果该组中有记录
                # 上一个有记录的组中的尾记录链接到该组头记录
                c.next = f[i]
                # 尾记录后移
                c = e[i]
        # 清空最后一条记录的next指针
        c.next = None

    cur = r
    # 将待排序列生成链表
    for v in a:
        node = Node(keys=[int(u) for u in str(v).zfill(d)], _next=None)
        cur.next = node
        cur = cur.next

    # 依次对关键字进行分配和收集操作
    for idx in range(d - 1, -1, -1):
        # 重新初始化收尾记录数组
        f, e = ([None for _ in range(_RADIX)] for _ in range(2))
        # 分配
        distribute(idx)
        # 收集
        collect()

    # 此时待排序列链表已经有序，将记录恢复到原序列中
    cur = r.next
    for ai in range(len(a)):
        a[ai] = int(''.join([str(v) for v in cur.keys]))
        cur = cur.next


# 桶排序
def bucket_sort(a, reverse=False):
    """
    桶排序
    假设输入数据服从均匀分布，假设输入是由一个随机过程产生，该过程将元素均匀、独立的分布在[0, 1)区间上。
    将[0, 1)区间划分为n个相同大小的子区间，称为桶。然后将n个输入数分别分配在各个桶中。
    先对每个桶中的数进行排序，然后遍历每个桶，按照次序把各个桶中的元素列出来即可。
    :param a:
    :param reverse:
    :return:
    """
    n = len(a)  # 待排记录总数
    b = [[] for _ in range(n)]  # 初始化桶
    # 将记录分配到桶中
    for v in a:
        b[int(n * v)].append(v)
    # 对每个桶分别进行排序
    for v in b:
        if v and len(v) > 0:
            comparison_sorting.straight_insertion_sort(v)

    # 按照次序把每个桶中的记录列出来，并返回
    return [u for v in (b[::-1] if reverse else b) if v and len(v) > 0 for u in (v[::-1] if reverse else v)]
