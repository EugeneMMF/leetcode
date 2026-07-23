from typing import List
import sys
sys.setrecursionlimit(1 << 20)
class Solution:
    def countGoodNodes(self, edges: List[List[int]]) -> int:
        n = len(edges) + 1
        g = [[] for _ in range(n)]
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)
        res = 0
        def dfs(u, p):
            nonlocal res
            total = 1
            child_size = None
            good = True
            for v in g[u]:
                if v == p:
                    continue
                sz = dfs(v, u)
                total += sz
                if child_size is None:
                    child_size = sz
                elif child_size != sz:
                    good = False
            if good:
                res += 1
            return total
        dfs(0, -1)
        return res