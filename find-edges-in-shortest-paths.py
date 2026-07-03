class Solution:
    def findAnswer(self, n: int, edges: List[List[int]]) -> List[bool]:
        from heapq import heappush, heappop
        INF = 10**18
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))
        def dijkstra(start):
            dist = [INF] * n
            dist[start] = 0
            pq = [(0, start)]
            while pq:
                d, u = heappop(pq)
                if d != dist[u]:
                    continue
                for v, w in adj[u]:
                    nd = d + w
                    if nd < dist[v]:
                        dist[v] = nd
                        heappush(pq, (nd, v))
            return dist
        dist0 = dijkstra(0)
        distT = dijkstra(n - 1)
        d = dist0[n - 1]
        ans = []
        for u, v, w in edges:
            if dist0[u] + w + distT[v] == d or dist0[v] + w + distT[u] == d:
                ans.append(True)
            else:
                ans.append(False)
        return ans