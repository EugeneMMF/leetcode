class Solution:
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        adj = [set() for _ in range(n + 1)]
        deg = [0] * (n + 1)
        for u, v in edges:
            adj[u].add(v)
            adj[v].add(u)
            deg[u] += 1
            deg[v] += 1
        min_deg = float('inf')
        for i in range(1, n + 1):
            for j in adj[i]:
                if j <= i:
                    continue
                common = adj[i] & adj[j]
                for k in common:
                    if k <= j:
                        continue
                    cur = deg[i] + deg[j] + deg[k] - 6
                    if cur < min_deg:
                        min_deg = cur
        return -1 if min_deg == float('inf') else min_deg