import sys

class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        n = len(s)

        cost = [[0] * n for _ in range(n)]

        for l in range(2, n + 1):
            for i in range(n - l + 1):
                j = i + l - 1
                
                cost[i][j] = cost[i+1][j-1]
                if s[i] != s[j]:
                    cost[i][j] += 1
        
        dp = [[sys.maxsize] * (k + 1) for _ in range(n)]

        for i in range(n):
            dp[i][1] = cost[0][i]

        for j in range(2, k + 1):
            for i in range(j - 1, n):
                for p in range(j - 2, i):
                    if dp[p][j-1] != sys.maxsize:
                        dp[i][j] = min(dp[i][j], dp[p][j-1] + cost[p+1][i])
        
        return dp[n-1][k]
