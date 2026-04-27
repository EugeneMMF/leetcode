from typing import List
from functools import lru_cache

class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        MOD = 10**9 + 7
        n = len(locations)

        @lru_cache(None)
        def dfs(city, f):
            res = 1 if city == finish else 0
            for nxt in range(n):
                if nxt != city:
                    cost = abs(locations[city] - locations[nxt])
                    if f >= cost:
                        res += dfs(nxt, f - cost)
            return res % MOD

        return dfs(start, fuel)
