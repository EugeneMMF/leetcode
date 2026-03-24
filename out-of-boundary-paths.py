
class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD = 10**9 + 7
        
        dp = [[0] * n for _ in range(m)]
        dp[startRow][startColumn] = 1
        
        out_of_bounds_paths = 0
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        for _ in range(maxMove):
            next_dp = [[0] * n for _ in range(m)]
            
            for r in range(m):
                for c in range(n):
                    if dp[r][c] > 0:
                        for dr, dc in directions:
                            nr, nc = r + dr, c + dc
                            
                            if 0 <= nr < m and 0 <= nc < n:
                                next_dp[nr][nc] = (next_dp[nr][nc] + dp[r][c]) % MOD
                            else:
                                out_of_bounds_paths = (out_of_bounds_paths + dp[r][c]) % MOD
            
            dp = next_dp
            
        return out_of_bounds_paths
