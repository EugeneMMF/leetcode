import collections
from typing import List

class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def topo(n, cond):
            adj = [[] for _ in range(n + 1)]
            indeg = [0] * (n + 1)
            for a, b in cond:
                adj[a].append(b)
                indeg[b] += 1
            q = collections.deque([i for i in range(1, n + 1) if indeg[i] == 0])
            order = []
            while q:
                u = q.popleft()
                order.append(u)
                for v in adj[u]:
                    indeg[v] -= 1
                    if indeg[v] == 0:
                        q.append(v)
            if len(order) != n:
                return []
            return order

        row_order = topo(k, rowConditions)
        if not row_order:
            return []
        col_order = topo(k, colConditions)
        if not col_order:
            return []

        row_pos = [0] * (k + 1)
        col_pos = [0] * (k + 1)
        for idx, num in enumerate(row_order):
            row_pos[num] = idx
        for idx, num in enumerate(col_order):
            col_pos[num] = idx

        matrix = [[0] * k for _ in range(k)]
        for num in range(1, k + 1):
            matrix[row_pos[num]][col_pos[num]] = num
        return matrix