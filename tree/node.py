# coding=utf-8


class Node(object):
    """
    AVL Node
    """
    parent = None
    left = None
    right = None

    def __init__(self, key, data=None):
        self.key = key
        self.data = data
