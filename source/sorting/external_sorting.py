# -*- coding: utf-8 -*-

from .comparison_sorting import merge_sort
from source.tree.winner_loser_tree import LoserTree


def multi_ways_balance_merge_sort(a):
    """
    多路平衡归并排序
    - 多用于外部排序
    - 使用多维数组模拟外部存储归并段
    - 使用loser tree来实现多路归并
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
