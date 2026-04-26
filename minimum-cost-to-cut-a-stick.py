class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts = sorted(cuts)
        cuts = [0] + cuts + [n]
        from functools import lru_cache
        @lru_cache(None)
        def dp(i, j):
            if i + 1 >= j:
                return 0
            best = 10**18
            cost = cuts[j] - cuts[i]
            for k in range(i + 1, j):
                cur = cost + dp(i, k) + dp(k, j)
                if cur < best:
                    best = cur
            return best
        return dp(0, len(cuts) - 1)
