class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        n = len(cost)
        INF = 10**18
        dp = [INF] * (n + 1)
        dp[0] = 0
        for c, t in zip(cost, time):
            w = t + 1
            for j in range(n, -1, -1):
                if dp[j] == INF:
                    continue
                nj = j + w
                if nj > n:
                    nj = n
                if dp[nj] > dp[j] + c:
                    dp[nj] = dp[j] + c
        return dp[n]