class Skiplist:
    import random
    class Node:
        __slots__ = ('val','forward')
        def __init__(self, val, level):
            self.val = val
            self.forward = [None]*level
    def __init__(self):
        self.max_level = 16
        self.p = 0.5
        self.level = 1
        self.head = self.Node(-1, self.max_level)
    def random_level(self):
        lvl = 1
        while self.random.random() < self.p and lvl < self.max_level:
            lvl += 1
        return lvl
    def search(self, target: int) -> bool:
        cur = self.head
        for i in range(self.level-1, -1, -1):
            while cur.forward[i] and cur.forward[i].val < target:
                cur = cur.forward[i]
        cur = cur.forward[0]
        return cur is not None and cur.val == target
    def add(self, num: int) -> None:
        update = [None]*self.max_level
        cur = self.head
        for i in range(self.level-1, -1, -1):
            while cur.forward[i] and cur.forward[i].val < num:
                cur = cur.forward[i]
            update[i] = cur
        lvl = self.random_level()
        if lvl > self.level:
            for i in range(self.level, lvl):
                update[i] = self.head
            self.level = lvl
        node = self.Node(num, lvl)
        for i in range(lvl):
            node.forward[i] = update[i].forward[i]
            update[i].forward[i] = node
    def erase(self, num: int) -> bool:
        update = [None]*self.max_level
        cur = self.head
        for i in range(self.level-1, -1, -1):
            while cur.forward[i] and cur.forward[i].val < num:
                cur = cur.forward[i]
            update[i] = cur
        cur = cur.forward[0]
        if not cur or cur.val != num:
            return False
        for i in range(self.level):
            if update[i].forward[i] != cur:
                break
            update[i].forward[i] = cur.forward[i]
        while self.level > 1 and not self.head.forward[self.level-1]:
            self.level -= 1
        return True
