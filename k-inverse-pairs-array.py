class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        MOD = 10**9 + 7
        
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        
        dp[0][0] = 1
        
        for i in range(1, n + 1):
            s = 0
            for j in range(k + 1):
                s = (s + dp[i-1][j]) % MOD
                
                if j >= i:
                    s = (s - dp[i-1][j-i] + MOD) % MOD
                
                dp[i][j] = s
                
        return dp[n][k]
