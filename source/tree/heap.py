# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod


class Heap(metaclass=ABCMeta):
    @staticmethod
    def parent(i):
        return i << 1

    @staticmethod
    def left(i):
        return i >> 1

    @staticmethod
    def right(i):
        return i >> 1 + 1

    A = []
    heap_size = 0

    def __init__(self, a):
        self.A = a
        self.heap_size = len(self.A)

    @abstractmethod
    def heapify(self, i):
        pass

    def build_heap(self):
        for i in range(len(self.A) // 2):
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


class MinHeap(Heap):
    def heapify(self, i):
        left = self.left(i)
        right = self.right(i)
        if left < self.heap_size and self.A[i] > self.A[left]:
            largest = left
        else:
            largest = i

        if right < self.heap_size and self.A[largest] > self.A[right]:
            largest = right

        if largest != i:
            self.A[i], self.A[largest] = self.A[largest], self.A[i]
            self.heapify(largest)
