class Solution:
    def areConnected(self, n, threshold, queries):
        parent = list(range(n + 1))
        rank = [0] * (n + 1)
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        def union(x, y):
            rx, ry = find(x), find(y)
            if rx == ry:
                return
            if rank[rx] < rank[ry]:
                parent[rx] = ry
            elif rank[rx] > rank[ry]:
                parent[ry] = rx
            else:
                parent[ry] = rx
                rank[rx] += 1
        for d in range(threshold + 1, n + 1):
            step = d
            first = d * 2
            for m in range(first, n + 1, step):
                union(d, m)
        return [find(a) == find(b) for a, b in queries]
