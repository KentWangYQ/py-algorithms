# -*- coding: utf-8 -*-


# region CUT ROD
def memoized_cut_rod(p, n):
    """
    钢条切个问题

    动态规划实现
    待备忘录的自顶向下法(top-down with memoization)
    :param p:
    :param n:
    :return:
    """
    r = [float('-inf')] * n
    return _memoized_cut_rod_aux(p, n, r)


def _memoized_cut_rod_aux(p, n, r):
    if r[n - 1] >= 0:
        return r[n - 1]

    if n == 0:
        q = 0
    else:
        q = float('-inf')
        for i in range(n):
            q = max(q, p[i] + _memoized_cut_rod_aux(p, n - i - 1, r))
    r[n - 1] = q
    return q


def bottom_up_cut_rod(p, n):
    """
    钢条切个问题

    动态规划实现
    自底向上法(bottom-up)
    :param p:
    :param n:
    :return:
    """
    r = [float('-inf')] * (n + 1)
    r[0] = 0
    for i in range(1, n + 1):
        q = float('-inf')
        for j in range(i + 1):
            q = max(q, p[j - 1] + r[i - j])
        r[i] = q
    return r[n]
# endregion
