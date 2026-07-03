from typing import List

class Solution:
    def numberOfRightTriangles(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        n = len(grid)
        m = len(grid[0])
        row_counts = [0] * n
        col_counts = [0] * m
        for i in range(n):
            for j in range(m):
                if grid[i][j]:
                    row_counts[i] += 1
                    col_counts[j] += 1
        total = 0
        for i in range(n):
            rc = row_counts[i] - 1
            if rc <= 0:
                continue
            for j in range(m):
                if grid[i][j]:
                    cc = col_counts[j] - 1
                    if cc > 0:
                        total += rc * cc
        return total
