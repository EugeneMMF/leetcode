import sys
from typing import List

class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        graph = [[] for _ in range(n)]
        for a, b in richer:
            graph[b].append(a)
        memo = [-1] * n
        sys.setrecursionlimit(10000)
        def dfs(x: int) -> int:
            if memo[x] != -1:
                return memo[x]
            ans = x
            for y in graph[x]:
                cand = dfs(y)
                if quiet[cand] < quiet[ans]:
                    ans = cand
            memo[x] = ans
            return ans
        return [dfs(i) for i in range(n)]
