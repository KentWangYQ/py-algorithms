# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod

from .complete_binary_tree import CompleteBinaryTree


class Heap(CompleteBinaryTree, metaclass=ABCMeta):

    A = []
    heap_size = 0

    def __init__(self, a=None):
        self.A = a or []
        self.heap_size = len(self.A)
        self.build_heap()

    @abstractmethod
    def heapify(self, i):
        pass

    @abstractmethod
    def heap_check(self):
        pass

    def build_heap(self):
        self.heap_size = len(self.A)
        for i in range(self.heap_size // 2 - 1, -1, -1):
            self.heapify(i)

    def heap_sort(self):
        for i in range(len(self.A) - 1, 0, -1):
            self.A[0], self.A[i] = self.A[i], self.A[0]
            self.heap_size -= 1
            self.heapify(0)


class MaxHeap(Heap):
    def heapify(self, i):
        left = self.left(i)
        right = self.right(i)
        if left < self.heap_size and self.A[i] < self.A[left]:
            largest = left
        else:
            largest = i
        if right < self.heap_size and self.A[largest] < self.A[right]:
            largest = right

        if largest != i:
            self.A[i], self.A[largest] = self.A[largest], self.A[i]
            self.heapify(largest)

    def heap_check(self):
        for i in range(self.heap_size // 2):
            left = self.left(i)
            right = self.right(i)
            if self.A[left] > self.A[i] or (right < self.heap_size and self.A[right] > self.A[i]):
                return False
        return True

    def maximum(self):
        return self.A[0]

    def extract_max(self):
        _max = None
        if self.heap_size > 0:
            _max = self.A[0]
            self.A[0] = self.A[self.heap_size - 1]
            self.heap_size -= 1
            self.heapify(0)
        return _max

    def increase_key(self, i, key):
        assert key >= self.A[i], ValueError('New key is smaller than current key!')
        self.A[i] = key
        parent = self.parent(i)
        while i > 0 and self.A[i] > self.A[parent]:
            self.A[i], self.A[parent] = self.A[parent], self.A[i]
            i = parent
            parent = self.parent(i)

    def insert(self, key):
        if self.heap_size == len(self.A):
            self.A.append(float('-inf'))
        else:
            self.A[self.heap_size] = float('-inf')

        self.heap_size += 1
        self.increase_key(self.heap_size - 1, key)


class MinHeap(Heap):
    def heapify(self, i):
        left = self.left(i)
        right = self.right(i)
        if left < self.heap_size and self.A[i] > self.A[left]:
            least = left
        else:
            least = i

        if right < self.heap_size and self.A[least] > self.A[right]:
            least = right

        if least != i:
            self.A[i], self.A[least] = self.A[least], self.A[i]
            self.heapify(least)

    def heap_check(self):
        for i in range(self.heap_size // 2):
            left = self.left(i)
            right = self.right(i)
            if self.A[left] < self.A[i] or (right < self.heap_size and self.A[right] < self.A[i]):
                return False
        return True

    def minimum(self):
        return self.A[0]

    def extract_min(self):
        _min = None
        if self.heap_size > 0:
            _min = self.A[0]
            self.A[0] = self.A[self.heap_size - 1]
            self.heap_size -= 1
            self.heapify(0)
        return _min

    def decrease_key(self, i, key):
        assert self.A[i] > key, ValueError('New key is greater than current key!')
        self.A[i] = key
        parent = self.parent(i)
        while i > 0 and self.A[i] < self.A[parent]:
            self.A[i], self.A[parent] = self.A[parent], self.A[i]
            i = parent
            parent = self.parent(i)

    def insert(self, key):
        if self.heap_size == len(self.A):
            self.A.append(float('inf'))
        else:
            self.A[self.heap_size] = float('inf')
        self.heap_size += 1
        self.decrease_key(self.heap_size - 1, key)


class MaxPriorityQueue(MaxHeap):
    pass


class MinPriorityQueue(MinHeap):
    pass
