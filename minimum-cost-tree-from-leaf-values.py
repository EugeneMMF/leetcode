class Solution:
    def mctFromLeafValues(self, arr: list[int]) -> int:
        n = len(arr)
        
        max_val = [[0] * n for _ in range(n)]
        for i in range(n):
            max_val[i][i] = arr[i]
            for j in range(i + 1, n):
                max_val[i][j] = max(max_val[i][j-1], arr[j])
                
        dp = [[float('inf')] * n for _ in range(n)]
        
        for i in range(n):
            dp[i][i] = 0
            
        for length_L in range(2, n + 1):
            for i in range(n - length_L + 1):
                j = i + length_L - 1
                
                for k in range(i, j):
                    cost = dp[i][k] + dp[k+1][j] + max_val[i][k] * max_val[k+1][j]
                    dp[i][j] = min(dp[i][j], cost)
                    
        return dp[0][n-1]
