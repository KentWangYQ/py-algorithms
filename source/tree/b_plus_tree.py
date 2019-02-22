# -*- coding: utf-8 -*-


class BPNode(object):
    keys = []
    values = None
    c = []
    n = 0
    is_leaf = False
    next = None

    def __init__(self, t=5, is_leaf=False):
        self.keys = [None] * (2 * t - 1)
        self.c = [None] * (2 * t - 1)
        self.is_leaf = is_leaf
        if self.is_leaf:
            self.values = [None] * (2 * t - 1)

    def insert_key(self, i, k):
        j = self.n - 1
        while j >= i:
            self.keys[j + 1] = self.keys[j]
            j -= 1
        self.keys[i] = k
        self.n += 1

    def insert_value(self, i, v):
        j = len([value for value in self.values if value is not None]) - 1
        while j >= i:
            self.values[j + 1] = self.values[j]
            j -= 1

        self.values[i] = v

    def insert_c(self, i, cn):
        j = len([c for c in self.c if c]) - 1
        while j >= i:
            self.c[j + 1] = self.c[j]
            j -= 1
        self.c[i] = cn

    def append_key(self, k):
        self.keys[self.n] = k
        self.n += 1

    def append_value(self, v):
        idx = len([value for value in self.values if value is not None])
        self.values[idx] = v

    def append_c(self, cn):
        idx = len([c for c in self.c if c])
        self.c[idx] = cn

    def del_key(self, i):
        key = self.keys[i]
        while i < self.n - 1:
            self.keys[i] = self.keys[i + 1]
            i += 1
        self.pop_key()
        return key

    def del_value(self, i):
        value = self.values[i]
        idx = len([value for value in self.values if value is not None]) - 1
        while i < idx:
            self.values[i] = self.values[i + 1]
            i += 1
        self.pop_value()
        return value

    def del_c(self, i):
        c = self.c[i]
        idx = len([c for c in self.c if c]) - 1
        while i < idx:
            self.c[i] = self.c[i + 1]
            i += 1
        self.pop_c()
        return c

    def pop_key(self):
        key = self.keys[self.n - 1]
        self.keys[self.n - 1] = None
        self.n -= 1
        return key

    def pop_value(self):
        idx = len([value for value in self.values if value is not None]) - 1
        value = self.values[idx]
        self.values[idx] = None
        return value

    def pop_c(self):
        idx = len([c for c in self.c if c]) - 1
        c = self.c[idx]
        self.c[idx] = None
        return c


class BPTree(object):
    root = None
    head = None

    def __init__(self, t=2):
        self.t = t
        self.create()

    def create(self):
        x = ALLOCATE_NODE(t=self.t, is_leaf=True)
        DISK_WRITE(x)
        self.root = x
        self.head = x

    def tree_walk(self):
        keys = []
        p = self.head
        while p:
            keys += [key for key in p.keys if key is not None]
            p = p.next
        return keys

    def _split_node(self, x, i):
        y = x.c[i]
        z = ALLOCATE_NODE(t=self.t, is_leaf=y.is_leaf)

        for _ in range(self.t):
            z.insert_key(0, y.pop_key())
            z.insert_c(0, y.pop_c())
            if y.is_leaf:
                z.insert_value(0, y.pop_value())

        x.insert_key(i + 1, z.keys[0])
        x.insert_c(i + 1, z)

        if y.is_leaf:
            z.next, y.next = y.next, z

        DISK_WRITE(x)
        DISK_WRITE(y)
        DISK_WRITE(z)

    def _merge_node(self, x, i):
        y = x.c[i]  # type:BPNode
        l_bro = x.c[i - 1] if i > 0 else None  # type:BPNode
        r_bro = x.c[i + 1] if i < x.n - 1 else None  # type:BPNode

        if l_bro and l_bro.n <= self.t:
            while y.n > 0:
                l_bro.append_key(y.del_key(0))
                l_bro.append_c(y.del_c(0))
                if y.is_leaf:
                    l_bro.append_value((y.del_value(0)))

            if y.is_leaf:
                l_bro.next = y.next

            x.del_key(i)
            x.del_c(i)
            return True
        elif r_bro and r_bro.n <= self.t:
            while r_bro.n > 0:
                y.append_key(r_bro.del_key(0))
                y.append_c(r_bro.del_c(0))
                if y.is_leaf:
                    y.append_value(r_bro.del_value(0))

            if y.is_leaf:
                y.next = r_bro.next

            x.del_key(i + 1)
            x.del_c(i + 1)
            return True

        return False

    def _rotation(self, x, i):
        r = x.c[i]  # type: BPNode
        l_bro = x.c[i - 1] if i > 0 else None  # type: BPNode
        r_bro = x.c[i + 1] if i < x.n - 1 else None  # type: BPNode

        # 兄弟结点至少有两个空位置才进行旋转，
        # 否则可能出现两个相邻兄弟结点相互旋转的死循环
        if l_bro and l_bro.n < 2 * self.t - 2:
            l_bro.append_key(r.del_key(0))
            l_bro.append_c(r.del_c(0))
            if r.is_leaf:
                l_bro.append_value(r.del_value(0))
            x.keys[i] = x.c[i].keys[0]
            return True
        elif r_bro and r_bro.n < 2 * self.t - 2:
            r_bro.insert_key(0, r.pop_key())
            r_bro.insert_c(0, r.pop_c())
            if r.is_leaf:
                r_bro.insert_value(0, r.pop_value())
            x.keys[i + 1] = x.c[i + 1].keys[0]
            return True
        return False

    def _de_rotation(self, x, i):
        r = x.c[i]  # type:BPNode
        l_bro = x.c[i - 1] if i > 0 else None  # type: BPNode
        r_bro = x.c[i + 1] if i < x.n - 1 else None  # type: BPNode

        if l_bro and l_bro.n > self.t - 1:
            r.insert_key(0, l_bro.pop_key())
            r.insert_c(0, l_bro.pop_c())
            if r.is_leaf:
                r.insert_value(0, l_bro.pop_value())
            x.keys[i] = x.c[i].keys[0]
            return True
        elif r_bro and r_bro.n > self.t - 1:
            r.append_key(r_bro.del_key(0))
            r.append_c(r_bro.del_c(0))
            if r.is_leaf:
                r.append_value(r_bro.del_value(0))
            x.keys[i + 1] = x.c[i + 1].keys[0]
            return True
        return False

    def _insert_non_full(self, x, k, v):

        if x.is_leaf:
            i = x.n - 1
            while i >= 0 and k < x.keys[i]:
                i -= 1
            i += 1
            x.insert_key(i, k)
            x.insert_value(i, v)
            DISK_WRITE(x)
        else:
            if k < x.keys[0]:
                x.keys[0] = k
                DISK_WRITE(x)

            i = x.n - 1
            while i >= 0 and k < x.keys[i]:
                i -= 1

            DISK_READ(x.c[i])
            if x.c[i].n >= 2 * self.t - 1:
                if not self._rotation(x, i):
                    self._split_node(x, i)

                self._insert_non_full(x, k, v)
            else:
                self._insert_non_full(x.c[i], k, v)

    def insert(self, k, v):
        r = self.root

        if r.n >= 2 * self.t - 1:
            s = ALLOCATE_NODE(t=self.t, is_leaf=False)
            self.root = s
            s.c[0] = r
            s.insert_key(0, r.keys[0])
            self._split_node(s, 0)
            DISK_WRITE(s)

        self._insert_non_full(self.root, k, v)

    def delete(self, x, k):
        i = x.n - 1
        while i >= 0 and k < x.keys[i]:
            i -= 1

        if x.is_leaf:
            idx = x.keys.index(k)
            if idx > -1:
                x.del_key(idx)
                x.del_value(idx)
        else:
            if i < 0:
                # key不在该树中
                return

            if x.c[i].n <= self.t - 1:
                if not self._de_rotation(x, i):
                    self._merge_node(x, i)
                    if i > x.n - 1 or k < x.keys[i]:
                        i -= 1

            if k == x.keys[i]:
                y, j = successor(x, i)
                x.keys[i] = y.keys[j]

            self.delete(x.c[i], k)


def search(x, k):
    i = x.n - 1
    while i >= 0 and k < x.keys[i]:
        i -= 1

    if i < 0:
        return None, -1

    if x.is_leaf:
        if k == x.keys[i]:
            return x, i
        else:
            return None, -1

    return search(x.c[i], k)


def minimum(x):
    while x.c[0]:
        x = x.c[0]
    return x, 0


def maximum(x):
    while x.c[x.n - 1]:
        x = x.c[x.n - 1]
    return x, x.n - 1


def predecessor(x, i):
    if x.is_leaf:
        if i <= 0:
            return None, -1
        return x, i - 1
    return maximum(x.c[i])


def successor(x, i):
    if x.is_leaf:
        if i >= x.n - 1:
            return None, -1
        return x, i + 1
    y, j = minimum(x.c[i])
    return y, j + 1


def ALLOCATE_NODE(t=3, is_leaf=False):
    return BPNode(t=t, is_leaf=is_leaf)


def DISK_READ(x):
    pass


def DISK_WRITE(x):
    pass
