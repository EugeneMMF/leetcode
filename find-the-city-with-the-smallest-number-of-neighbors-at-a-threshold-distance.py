from typing import List

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        INF = 10**9
        dist = [[INF]*n for _ in range(n)]
        for i in range(n):
            dist[i][i] = 0
        for u, v, w in edges:
            dist[u][v] = w
            dist[v][u] = w
        for k in range(n):
            dk = dist[k]
            for i in range(n):
                di = dist[i]
                ik = di[k]
                if ik == INF:
                    continue
                for j in range(n):
                    nd = ik + dk[j]
                    if nd < di[j]:
                        di[j] = nd
        best_city = -1
        best_cnt = n + 1
        for i in range(n):
            cnt = sum(1 for j in range(n) if i != j and dist[i][j] <= distanceThreshold)
            if cnt < best_cnt or (cnt == best_cnt and i > best_city):
                best_cnt = cnt
                best_city = i
        return best_city
