from typing import List

class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        import sys
        sys.setrecursionlimit(10**6)
        g = [[] for _ in range(n)]
        for u, v in connections:
            g[u].append(v)
            g[v].append(u)
        ids = [-1] * n
        low = [0] * n
        timer = 0
        res = []
        def dfs(at, parent):
            nonlocal timer
            ids[at] = low[at] = timer
            timer += 1
            for to in g[at]:
                if to == parent:
                    continue
                if ids[to] == -1:
                    dfs(to, at)
                    low[at] = low[at] if low[at] < low[to] else low[to]
                    if low[to] > ids[at]:
                        res.append([at, to])
                else:
                    low[at] = low[at] if low[at] < ids[to] else ids[to]
        for i in range(n):
            if ids[i] == -1:
                dfs(i, -1)
        return res
