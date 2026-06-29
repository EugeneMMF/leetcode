from typing import List

class Solution:
    def numberOfSets(self, n: int, maxDistance: int, roads: List[List[int]]) -> int:
        INF = 10**9
        adj = [[INF]*n for _ in range(n)]
        for i in range(n):
            adj[i][i] = 0
        for u, v, w in roads:
            if w < adj[u][v]:
                adj[u][v] = adj[v][u] = w
        count = 0
        total = 1 << n
        for mask in range(total):
            nodes = [i for i in range(n) if mask >> i & 1]
            m = len(nodes)
            if m <= 1:
                count += 1
                continue
            dist = [[INF]*n for _ in range(n)]
            for i in nodes:
                dist[i][i] = 0
                for j in nodes:
                    if adj[i][j] < INF:
                        dist[i][j] = adj[i][j]
            for k in nodes:
                dk = dist[k]
                for i in nodes:
                    di = dist[i]
                    ik = di[k]
                    if ik == INF:
                        continue
                    for j in nodes:
                        nd = ik + dk[j]
                        if nd < di[j]:
                            di[j] = nd
            ok = True
            for i in nodes:
                di = dist[i]
                for j in nodes:
                    if di[j] > maxDistance:
                        ok = False
                        break
                if not ok:
                    break
            if ok:
                count += 1
        return count
