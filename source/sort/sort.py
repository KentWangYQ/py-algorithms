# -*- coding: utf-8 -*-
import random

from source.tree.heap import MinHeap, MaxHeap


def insertion_sort(a, reverse=False):
    for i in range(1, len(a)):
        k = i
        for _ in range(i - 1, -1, -1):
            compare = a[k] > a[k - 1] if reverse else a[k] < a[k - 1]

            if compare:
                a[k], a[k - 1] = a[k - 1], a[k]
                # 注意在交换位置后迁移指针
                k -= 1
            else:
                break


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
