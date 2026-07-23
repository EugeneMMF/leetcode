from collections import deque
from typing import List

class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(n)]
        for i in range(n - 1):
            adj[i].append(i + 1)
        res = []
        for u, v in queries:
            adj[u].append(v)
            dist = [-1] * n
            dq = deque([0])
            dist[0] = 0
            while dq:
                x = dq.popleft()
                if x == n - 1:
                    break
                for y in adj[x]:
                    if dist[y] == -1:
                        dist[y] = dist[x] + 1
                        dq.append(y)
            res.append(dist[n - 1])
        return res
