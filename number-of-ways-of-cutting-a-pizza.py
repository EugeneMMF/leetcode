class Solution:
    def ways(self, pizza, k):
        from functools import lru_cache
        MOD = 10**9 + 7
        rows, cols = len(pizza), len(pizza[0])
        ps = [[0] * (cols + 1) for _ in range(rows + 1)]
        for i in range(rows):
            for j in range(cols):
                ps[i+1][j+1] = ps[i][j+1] + ps[i+1][j] - ps[i][j] + (1 if pizza[i][j] == 'A' else 0)
        def hasApple(r1, c1, r2, c2):
            return (ps[r2+1][c2+1] - ps[r1][c2+1] - ps[r2+1][c1] + ps[r1][c1]) > 0
        @lru_cache(None)
        def dp(r, c, cuts):
            if not hasApple(r, c, rows-1, cols-1):
                return 0
            if cuts == 1:
                return 1
            ans = 0
            for nr in range(r+1, rows):
                if hasApple(r, c, nr-1, cols-1):
                    ans = (ans + dp(nr, c, cuts-1)) % MOD
            for nc in range(c+1, cols):
                if hasApple(r, c, rows-1, nc-1):
                    ans = (ans + dp(r, nc, cuts-1)) % MOD
            return ans
        return dp(0, 0, k)
