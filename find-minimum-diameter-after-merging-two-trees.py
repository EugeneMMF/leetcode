class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        def diameter(edges, n):
            if n == 1:
                return 0
            adj = [[] for _ in range(n)]
            for a, b in edges:
                adj[a].append(b)
                adj[b].append(a)
            from collections import deque
            def bfs(start):
                dist = [-1] * n
                dist[start] = 0
                q = deque([start])
                far = start
                while q:
                    u = q.popleft()
                    for v in adj[u]:
                        if dist[v] == -1:
                            dist[v] = dist[u] + 1
                            q.append(v)
                            if dist[v] > dist[far]:
                                far = v
                return far, dist[far]
            far1, _ = bfs(0)
            _, d = bfs(far1)
            return d
        n = len(edges1) + 1
        m = len(edges2) + 1
        d1 = diameter(edges1, n)
        d2 = diameter(edges2, m)
        return max(d1, d2, (d1 + 1) // 2 + (d2 + 1) // 2 + 1)
