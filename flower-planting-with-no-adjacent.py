from typing import List

class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(n)]
        for a, b in paths:
            a -= 1
            b -= 1
            adj[a].append(b)
            adj[b].append(a)
        res = [0] * n
        for i in range(n):
            used = [False] * 5
            for nb in adj[i]:
                col = res[nb]
                if col:
                    used[col] = True
            for c in range(1, 5):
                if not used[c]:
                    res[i] = c
                    break
        return res
