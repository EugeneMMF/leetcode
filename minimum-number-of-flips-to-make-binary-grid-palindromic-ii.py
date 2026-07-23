from typing import List

class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        base = 0
        groups = []
        for i in range((m + 1) // 2):
            for j in range((n + 1) // 2):
                coords = {(i, j), (i, n - 1 - j), (m - 1 - i, j), (m - 1 - i, n - 1 - j)}
                s = len(coords)
                ones = 0
                for x, y in coords:
                    ones += grid[x][y]
                if s == 4:
                    base += min(ones, 4 - ones)
                else:
                    groups.append((s, ones))
        INF = 10**18
        dp = [INF, INF, INF, INF]
        dp[0] = 0
        for s, ones in groups:
            c0 = ones
            c1 = s - ones
            d = s % 4
            ndp = [INF, INF, INF, INF]
            for r in range(4):
                v = dp[r]
                if v == INF:
                    continue
                if v + c0 < ndp[r]:
                    ndp[r] = v + c0
                nr = (r + d) % 4
                if v + c1 < ndp[nr]:
                    ndp[nr] = v + c1
            dp = ndp
        return base + dp[0]
