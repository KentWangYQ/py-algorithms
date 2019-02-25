# -*- coding: utf-8 -*-
from source.tree.heap import MinHeap, MaxHeap


def insertion_sort(a, reverse=False):
    k = None
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

    return a


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


def merge_sort(a, p, r, reverse=False):
    if p < r:
        q = (r + p) // 2
        merge_sort(a, p, q, reverse=reverse)
        merge_sort(a, q + 1, r, reverse=reverse)
        _merge(a, p, q, r, reverse=reverse)


def heap_sort(a, reverse=False):
    heap = (MinHeap if reverse else MaxHeap)(a)

    for i in range(len(heap.A) - 1, 0, -1):
        heap.A[0], heap.A[i] = heap.A[i], heap.A[0]
        heap.heap_size -= 1
        heap.heapify(i)

    return heap.A
