class Solution:
    def maxNumEdgesToRemove(self, n, edges):
        class DSU:
            __slots__ = ("parent", "rank", "components")
            def __init__(self, size):
                self.parent = list(range(size + 1))
                self.rank = [0] * (size + 1)
                self.components = size
            def find(self, x):
                while self.parent[x] != x:
                    self.parent[x] = self.parent[self.parent[x]]
                    x = self.parent[x]
                return x
            def union(self, a, b):
                ra = self.find(a)
                rb = self.find(b)
                if ra == rb:
                    return False
                if self.rank[ra] < self.rank[rb]:
                    ra, rb = rb, ra
                self.parent[rb] = ra
                if self.rank[ra] == self.rank[rb]:
                    self.rank[ra] += 1
                self.components -= 1
                return True
        alice = DSU(n)
        bob = DSU(n)
        used = 0
        for t, u, v in edges:
            if t == 3:
                if alice.union(u, v):
                    bob.union(u, v)
                    used += 1
        for t, u, v in edges:
            if t == 1:
                if alice.union(u, v):
                    used += 1
            elif t == 2:
                if bob.union(u, v):
                    used += 1
        if alice.components != 1 or bob.components != 1:
            return -1
        return len(edges) - used
