import typing
from typing import List

class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        total = 0
        m = len(grid)
        n = len(grid[0]) if m > 0 else 0
        for row in grid:
            total += sum(row)
        if total % 2 != 0:
            return False
        target = total // 2
        cum = 0
        if m >= 2:
            for i, row in enumerate(grid):
                cum += sum(row)
                if cum == target and i != m - 1:
                    return True
        if n >= 2:
            col_sums = [0] * n
            for row in grid:
                for j, val in enumerate(row):
                    col_sums[j] += val
            cum = 0
            for j, sum_col in enumerate(col_sums):
                cum += sum_col
                if cum == target and j != n - 1:
                    return True
        return False
