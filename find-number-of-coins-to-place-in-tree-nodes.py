class Solution:
    def placedCoins(self, edges: List[List[int]], cost: List[int]) -> List[int]:
        n = len(cost)
        adj = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        parent = [-1] * n
        order = []
        stack = [0]
        while stack:
            u = stack.pop()
            order.append(u)
            for v in adj[u]:
                if v != parent[u]:
                    parent[v] = u
                    stack.append(v)
        max_vals = [None] * n
        min_vals = [None] * n
        sz = [0] * n
        res = [0] * n
        for u in reversed(order):
            mv = [cost[u]]
            mv.sort(reverse=True)
            mv = mv[:3]
            mi = [cost[u]]
            mi.sort()
            mi = mi[:2]
            size = 1
            for v in adj[u]:
                if parent[v] == u:
                    size += sz[v]
                    mv += max_vals[v]
                    mv.sort(reverse=True)
                    mv = mv[:3]
                    mi += min_vals[v]
                    mi.sort()
                    mi = mi[:2]
            max_vals[u] = mv
            min_vals[u] = mi
            sz[u] = size
            if size < 3:
                res[u] = 1
            else:
                prod1 = mv[0] * mv[1] * mv[2] if len(mv) >= 3 else float('-inf')
                prod2 = mi[0] * mi[1] * mv[0] if len(mi) >= 2 and len(mv) >= 1 else float('-inf')
                best = max(prod1, prod2)
                res[u] = 0 if best < 0 else best
        return res