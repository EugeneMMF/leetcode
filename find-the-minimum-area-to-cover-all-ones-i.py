class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        min_row = len(grid)
        max_row = -1
        min_col = len(grid[0])
        max_col = -1
        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                if val == 1:
                    if i < min_row:
                        min_row = i
                    if i > max_row:
                        max_row = i
                    if j < min_col:
                        min_col = j
                    if j > max_col:
                        max_col = j
        return (max_row - min_row + 1) * (max_col - min_col + 1)
