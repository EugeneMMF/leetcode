class Solution:
    def cherryPickup(self, grid: list[list[int]]) -> int:
        n = len(grid)
        
        dp = [[[-float('inf')] * n for _ in range(n)] for _ in range(2 * n - 1)]
        
        dp[0][0][0] = grid[0][0]
        
        for k in range(1, 2 * n - 1):
            for r1 in range(n):
                c1 = k - r1
                
                if c1 < 0 or c1 >= n or grid[r1][c1] == -1:
                    continue
                
                for r2 in range(n):
                    c2 = k - r2
                    
                    if c2 < 0 or c2 >= n or grid[r2][c2] == -1:
                        continue
                    
                    current_cherries = 0
                    current_cherries += grid[r1][c1]
                    if r1 != r2 or c1 != c2:
                        current_cherries += grid[r2][c2]
                        
                    max_prev_cherries = -float('inf')
                    
                    if r1 > 0 and r2 > 0:
                        max_prev_cherries = max(max_prev_cherries, dp[k-1][r1-1][r2-1])
                    
                    if r1 > 0 and c2 > 0:
                        max_prev_cherries = max(max_prev_cherries, dp[k-1][r1-1][r2])
                        
                    if c1 > 0 and r2 > 0:
                        max_prev_cherries = max(max_prev_cherries, dp[k-1][r1][r2-1])
                        
                    if c1 > 0 and c2 > 0:
                        max_prev_cherries = max(max_prev_cherries, dp[k-1][r1][r2])
                        
                    if max_prev_cherries != -float('inf'):
                        dp[k][r1][r2] = current_cherries + max_prev_cherries
        
        result = dp[2 * n - 2][n - 1][n - 1]
        
        return max(0, result)
