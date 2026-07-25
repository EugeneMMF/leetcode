class Solution:
    def maximumAmount(self, coins):
        m, n = len(coins), len(coins[0])
        INF = -10**18
        dp = [[[INF] * 3 for _ in range(n)] for _ in range(m)]
        val = coins[0][0]
        dp[0][0][0] = val
        if val >= 0:
            dp[0][0][1] = val
        else:
            dp[0][0][1] = 0
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                for k in range(3):
                    best_no = INF
                    best_neu = INF
                    if i > 0:
                        if dp[i-1][j][k] > best_no:
                            best_no = dp[i-1][j][k]
                        if k > 0 and dp[i-1][j][k-1] > best_neu:
                            best_neu = dp[i-1][j][k-1]
                    if j > 0:
                        if dp[i][j-1][k] > best_no:
                            best_no = dp[i][j-1][k]
                        if k > 0 and dp[i][j-1][k-1] > best_neu:
                            best_neu = dp[i][j-1][k-1]
                    v = coins[i][j]
                    if v >= 0:
                        if best_no != INF:
                            dp[i][j][k] = best_no + v
                    else:
                        candidates = []
                        if best_no != INF:
                            candidates.append(best_no + v)
                        if k > 0 and best_neu != INF:
                            candidates.append(best_neu)
                        if candidates:
                            dp[i][j][k] = max(candidates)
        return max(dp[m-1][n-1])