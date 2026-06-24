class Solution:
    def longestString(self, x: int, y: int, z: int) -> int:
        from functools import lru_cache
        allowed = {
            0: [1, 2, 3],
            1: [2],
            2: [1, 3],
            3: [1, 3]
        }
        @lru_cache(None)
        def dfs(a, b, c, last):
            best = 0
            for t in allowed[last]:
                if t == 1 and a > 0:
                    best = max(best, 2 + dfs(a - 1, b, c, 1))
                if t == 2 and b > 0:
                    best = max(best, 2 + dfs(a, b - 1, c, 2))
                if t == 3 and c > 0:
                    best = max(best, 2 + dfs(a, b, c - 1, 3))
            return best
        return dfs(x, y, z, 0)
