class Solution:
    def minFallingPathSum(self, grid: list[list[int]]) -> int:
        n = len(grid)

        prev_dp_row = list(grid[0])

        for i in range(1, n):
            current_dp_row = [0] * n

            min1_val = float('inf')
            min1_idx = -1
            min2_val = float('inf')
            min2_idx = -1

            for k in range(n):
                if prev_dp_row[k] < min1_val:
                    min2_val = min1_val
                    min2_idx = min1_idx
                    min1_val = prev_dp_row[k]
                    min1_idx = k
                elif prev_dp_row[k] < min2_val:
                    min2_val = prev_dp_row[k]
                    min2_idx = k
            
            for j in range(n):
                if j == min1_idx:
                    current_dp_row[j] = grid[i][j] + min2_val
                else:
                    current_dp_row[j] = grid[i][j] + min1_val
            
            prev_dp_row = current_dp_row

        return min(prev_dp_row)
