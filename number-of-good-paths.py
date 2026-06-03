class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        n = len(vals)
        adj = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        parent = list(range(n))
        size = [1] * n
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        def union(x, y):
            rx, ry = find(x), find(y)
            if rx == ry:
                return
            if size[rx] < size[ry]:
                rx, ry = ry, rx
            parent[ry] = rx
            size[rx] += size[ry]
        nodes = sorted(range(n), key=lambda i: vals[i])
        ans = n
        i = 0
        while i < n:
            v = vals[nodes[i]]
            group = []
            while i < n and vals[nodes[i]] == v:
                group.append(nodes[i])
                i += 1
            for u in group:
                for v2 in adj[u]:
                    if vals[v2] <= vals[u]:
                        union(u, v2)
            comp = {}
            for u in group:
                r = find(u)
                comp[r] = comp.get(r, 0) + 1
            for cnt in comp.values():
                ans += cnt * (cnt - 1) // 2
        return ans
