# -*- coding: utf-8 -*-


def counting_sort(a, k, reverse=False):
    b = [0] * len(a)
    c = [0] * k
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
