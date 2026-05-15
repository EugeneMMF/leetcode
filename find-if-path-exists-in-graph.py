from typing import List
from collections import deque

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        visited = [False] * n
        visited[source] = True
        dq = deque([source])
        while dq:
            u = dq.popleft()
            for v in adj[u]:
                if not visited[v]:
                    if v == destination:
                        return True
                    visited[v] = True
                    dq.append(v)
        return False
