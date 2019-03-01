# -*- coding: utf-8 -*-

from source.sorting import comparison_sorting


def counting_sort(a, k, reverse=False):
    b = [0] * len(a)
    c = [0] * (k + 1)
    for v in a:
        c[v] += 1

    if reverse:
        for i in range(len(c) - 2, -1, -1):
            c[i] += c[i + 1]
    else:
        for i in range(1, len(c)):
            c[i] += c[i - 1]

    for v in a:
        b[c[v] - 1] = v
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


def bucket_sort(a, reverse=False):
    n = len(a)
    b = [[] for _ in range(n)]
    for v in a:
        b[int(n * v)].append(v)

    for v in b:
        if v and len(v) > 0:
            comparison_sorting.straight_insertion_sort(v)

    return [u for v in (b[::-1] if reverse else b) if v and len(v) > 0 for u in (v[::-1] if reverse else v)]
