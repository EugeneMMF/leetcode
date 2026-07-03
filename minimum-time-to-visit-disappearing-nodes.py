class Solution:
    def minimumTime(self, n: int, edges: List[List[int]], disappear: List[int]) -> List[int]:
        from heapq import heappush, heappop
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))
        INF = 10**18
        dist = [INF] * n
        if 0 < disappear[0]:
            dist[0] = 0
            heap = [(0, 0)]
        else:
            heap = []
        while heap:
            t, u = heappop(heap)
            if t != dist[u]:
                continue
            if t >= disappear[u]:
                continue
            for v, w in adj[u]:
                nt = t + w
                if nt < disappear[v] and nt < dist[v]:
                    dist[v] = nt
                    heappush(heap, (nt, v))
        return [d if d < INF else -1 for d in dist]