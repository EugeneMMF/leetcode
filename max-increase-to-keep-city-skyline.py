class Solution:
    def maxIncreaseKeepingSkyline(self, grid: list[list[int]]) -> int:
        n = len(grid)
        row_max = [0] * n
        col_max = [0] * n

        for r in range(n):
            for c in range(n):
                row_max[r] = max(row_max[r], grid[r][c])
                col_max[c] = max(col_max[c], grid[r][c])

        total_increase = 0
        for r in range(n):
            for c in range(n):
                max_height = min(row_max[r], col_max[c])
                total_increase += max_height - grid[r][c]

        return total_increase

