# -*- coding: utf-8 -*-


def sequential_search(a, key):
    for i, v in enumerate(a):
        if v == key:
            return i, v
    return -1, None


def binary_search(a, key):
    """
    折半查找
    - 只适用于有序表，且限于顺序存储结构
    :param a:
    :param key:
    :return:
    """
    low, high = 0, len(a) - 1

    while low <= high:
        mid = (low + high) // 2
        if a[mid] == key:
            return mid, a[mid]
        elif key < a[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return -1, None
