class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        MOD = 10**9 + 7
        adj = [[] for _ in range(n + 1)]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))
        import heapq
        dist = [10**18] * (n + 1)
        dist[n] = 0
        heap = [(0, n)]
        while heap:
            d, u = heapq.heappop(heap)
            if d != dist[u]:
                continue
            for v, w in adj[u]:
                nd = d + w
                if nd < dist[v]:
                    dist[v] = nd
                    heapq.heappush(heap, (nd, v))
        order = sorted(range(1, n + 1), key=lambda x: dist[x])
        dp = [0] * (n + 1)
        dp[n] = 1
        for u in order[1:]:
            s = 0
            du = dist[u]
            for v, _ in adj[u]:
                if du > dist[v]:
                    s += dp[v]
                    if s >= MOD:
                        s -= MOD
            dp[u] = s
        return dp[1] % MOD