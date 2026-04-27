class Solution:
    def connectTwoGroups(self, cost):
        size1, size2 = len(cost), len(cost[0])
        full = (1 << size2) - 1
        INF = float('inf')
        dp = [INF] * (1 << size2)
        dp[0] = 0
        for i in range(size1):
            ndp = [INF] * (1 << size2)
            for mask in range(1 << size2):
                cur = dp[mask]
                if cur == INF:
                    continue
                for j in range(size2):
                    nmask = mask | (1 << j)
                    val = cur + cost[i][j]
                    if val < ndp[nmask]:
                        ndp[nmask] = val
            dp = ndp
        mincol = [min(cost[i][j] for i in range(size1)) for j in range(size2)]
        ans = INF
        for mask in range(1 << size2):
            extra = 0
            for j in range(size2):
                if not (mask >> j) & 1:
                    extra += mincol[j]
            total = dp[mask] + extra
            if total < ans:
                ans = total
        return ans
