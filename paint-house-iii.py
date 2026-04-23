class Solution:
    def minCost(self, houses, cost, m, n, target):
        INF = 10**15
        dp = [[[INF] * (n + 1) for _ in range(target + 1)] for _ in range(m)]
        for i in range(m):
            allowed = [houses[i]] if houses[i] != 0 else range(1, n + 1)
            for c in allowed:
                cur = 0 if houses[i] != 0 else cost[i][c - 1]
                if i == 0:
                    if target >= 1:
                        dp[i][1][c] = cur
                else:
                    for t in range(1, target + 1):
                        for pc in range(1, n + 1):
                            prev = dp[i - 1][t][pc]
                            if prev == INF:
                                continue
                            nt = t + (c != pc)
                            if nt <= target:
                                val = prev + cur
                                if val < dp[i][nt][c]:
                                    dp[i][nt][c] = val
        ans = INF
        for c in range(1, n + 1):
            if dp[m - 1][target][c] < ans:
                ans = dp[m - 1][target][c]
        return -1 if ans == INF else ans
