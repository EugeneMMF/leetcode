class Solution:
    def maxProductPath(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        MOD = 10**9 + 7

        dp_max = [[float('-inf')] * n for _ in range(m)]
        dp_min = [[float('inf')] * n for _ in range(m)]

        dp_max[0][0] = grid[0][0]
        dp_min[0][0] = grid[0][0]

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue

                current_val = grid[i][j]

                if i > 0:
                    prev_max_up = dp_max[i-1][j]
                    prev_min_up = dp_min[i-1][j]

                    if current_val >= 0:
                        dp_max[i][j] = max(dp_max[i][j], prev_max_up * current_val)
                        dp_min[i][j] = min(dp_min[i][j], prev_min_up * current_val)
                    else:
                        dp_max[i][j] = max(dp_max[i][j], prev_min_up * current_val)
                        dp_min[i][j] = min(dp_min[i][j], prev_max_up * current_val)

                if j > 0:
                    prev_max_left = dp_max[i][j-1]
                    prev_min_left = dp_min[i][j-1]

                    if current_val >= 0:
                        dp_max[i][j] = max(dp_max[i][j], prev_max_left * current_val)
                        dp_min[i][j] = min(dp_min[i][j], prev_min_left * current_val)
                    else:
                        dp_max[i][j] = max(dp_max[i][j], prev_min_left * current_val)
                        dp_min[i][j] = min(dp_min[i][j], prev_max_left * current_val)

        result = dp_max[m-1][n-1]

        if result < 0:
            return -1
        else:
            return result % MOD

