class Solution:
    def minDistance(self, houses, k):
        houses.sort()
        n = len(houses)
        cost = [[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(i, n):
                m = (i + j) // 2
                total = 0
                for t in range(i, j+1):
                    total += abs(houses[t] - houses[m])
                cost[i][j] = total
        INF = 10**9
        dp = [[INF]*(k+1) for _ in range(n+1)]
        dp[0][0] = 0
        for i in range(1, n+1):
            for m in range(1, min(k, i)+1):
                for p in range(m-1, i):
                    val = dp[p][m-1] + cost[p][i-1]
                    if val < dp[i][m]:
                        dp[i][m] = val
        return dp[n][k]
