class Solution:
    def cherryPickup(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        from functools import lru_cache
        @lru_cache(None)
        def dp(r, c1, c2):
            if c1 < 0 or c1 >= cols or c2 < 0 or c2 >= cols:
                return -10**9
            res = grid[r][c1]
            if c2 != c1:
                res += grid[r][c2]
            if r != rows - 1:
                best = -10**9
                for nc1 in (c1 - 1, c1, c1 + 1):
                    for nc2 in (c2 - 1, c2, c2 + 1):
                        best = max(best, dp(r + 1, nc1, nc2))
                res += best
            return res
        return dp(0, 0, cols - 1)
