class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        n = len(roads) + 1
        adj = [[] for _ in range(n)]
        for a, b in roads:
            adj[a].append(b)
            adj[b].append(a)
        parent = [-1] * n
        order = []
        stack = [0]
        parent[0] = 0
        while stack:
            u = stack.pop()
            order.append(u)
            for v in adj[u]:
                if parent[v] == -1:
                    parent[v] = u
                    stack.append(v)
        size = [1] * n
        ans = 0
        for u in reversed(order):
            if u != 0:
                p = parent[u]
                ans += (size[u] + seats - 1) // seats
                size[p] += size[u]
        return ans