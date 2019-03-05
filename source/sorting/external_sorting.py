# -*- coding: utf-8 -*-

from .comparison_sorting import merge_sort
from source.tree.winner_loser_tree import LoserTree


def multi_ways_balance_merge_sort(a):
    """
    多路平衡归并排序
    - 多用于外部排序
    - 使用多维数组模拟外部存储归并段
    - 使用loser tree来实现多路归并
    - 归并的趟数跟路数k成反比，增加路数k可以调高效率
    :param a:
    :return:
    """
    SENTRY = float('inf')  # 哨兵，作为归并段的结尾
    leaves = []  # 每个归并段中的一个元素构成loser tree的原始序列
    b = []  # 输出归并段，此实现中简化为以为数组。实际情况下也需要对输出分段。
    for v in a:
        merge_sort(v)  # 归并段内排序，采用归并排序
        v.append(SENTRY)  # 每个归并段追加哨兵
        leaves.append(v[0])  # 每个归并段的首元素构成初始化loser tree的原始序列
        del v[0]  # 删除各归并段的首元素
    lt = LoserTree(leaves)  # 构建loser tree
    # 循环获取winner
    while True:
        i, v = lt.winner  # winner
        if v == SENTRY:
            # 排序结束
            break

        b.append(v)  # 将winner写入输出归并段
        lt.modify_key(i, a[i][0])  # winner所在的归并段的下一个元素更新入loser tree
        del a[i][0]  # 删除已处理数据
    return b  # 返回有序序列


def replacement_selection_sort(a, k):
    """
    置换选择排序
    - 归并的趟数与初始归并段数m成正比，因此减少m可以提高效率。
    - 使用loser tree实现置换选择。
    - 基本思路：假设内存工作区可容纳k条记录，FI为待排序列，FO初始归并段输出，WA内存工作区。
        1. FI的前k条输入WA，初始化loser tree。
        2. WA中选出最小值，MIN。
        3. MIN记如归并段输出。
        4. 若FI不为空，FI中下一条记录输入WA替代MIN的位置。
        5. WA中在比MIN大的记录中选出最小值，作为新的MIN。
        6. 重复3～5，直到选不出新的MIN，此时得到一个初始归并段。
        7. 重复2～6，直到WA为空，此时得到全部的初始归并段。
    - 之后使用多路归并对初始归并段进行排序。
    :param a: 待排序类
    :param k: 内存工作区可容纳记录条数
    :return:
    """

    # 定义数据结点，包含i(归并段序号)和v(记录值)
    # 其中i用于辅助置换选择过程
    class Node(object):
        def __init__(self, i, v):
            self.i = i
            self.v = v

    SENTRY = float('inf')  # 哨兵
    # 待排序列
    # 尾部追加k个哨兵，用于替换最终停留在loser tree中的k条记录
    # 实现步骤7中的清空WA
    fi = a + [SENTRY] * k
    fo = []  # 初始归并段
    # 使用fi中前k条记录初始化loser tree，作为第一批记录，归并段号默认为0
    loser_tree = LoserTree(a=[Node(0, v) for v in fi[:k]],
                           match=lambda a, b: a.i < b.i if a.i != b.i else a.v < b.v,
                           extremum=Node(float('-inf'), float('-inf')))
    temp = []  # 临时归并段
    i = 0  # 归并段序号
    j = k  # 待排序列消耗指针
    while True:
        wi, wv = loser_tree.winner  # loser tree的winner
        if wv.v == SENTRY:
            # 如果winner为哨兵，说明WA有效记录已清空
            # 写入最后一个初始归并段
            fo.append(temp)
            # 结束置换选择过程
            break

        if wv.i > i:
            # 如果winner的归并段号升级，说明上一个初始归并段结束
            # 写入初始归并段
            fo.append(temp)
            temp = []
            # 当前归并段号升级
            i += 1
        # winner记录值写入当前初始归并段
        temp.append(wv.v)

        # 使用fi中的当前记录替代winner，继续参加比赛
        if fi[j] < wv.v:
            # 如果fi当前元素小于winner值，则该记录只能进入下一个初始归并段
            # 其归并段号升级
            wv.i += 1
        # 替换值
        wv.v = fi[j]
        # 替换loser tree结点
        loser_tree.modify_key(wi, wv)
        # fi元素消耗指针后移
        j += 1

    # 对置换选择得到的初始归并段，进行多路平衡归并排序
    return multi_ways_balance_merge_sort(fo)
