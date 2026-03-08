class Solution:
    def getMoneyAmount(self, n: int) -> int:
        dp = [[0] * (n + 2) for _ in range(n + 2)]

        for length in range(2, n + 1):
            for i in range(1, n - length + 2):
                j = i + length - 1
                
                dp[i][j] = float('inf')
                
                for k in range(i, j + 1):
                    cost_if_lower = dp[i][k-1]
                    cost_if_higher = dp[k+1][j]
                    
                    current_guess_cost = k + max(cost_if_lower, cost_if_higher)
                    
                    dp[i][j] = min(dp[i][j], current_guess_cost)
        
        return dp[1][n]
