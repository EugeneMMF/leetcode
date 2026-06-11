from typing import List

class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        n = len(grid)
        pos = [None] * (n * n)
        for i in range(n):
            for j in range(n):
                pos[grid[i][j]] = (i, j)
        if pos[0] != (0, 0):
            return False
        for k in range(n * n - 1):
            r1, c1 = pos[k]
            r2, c2 = pos[k + 1]
            dr = abs(r2 - r1)
            dc = abs(c2 - c1)
            if not ((dr == 1 and dc == 2) or (dr == 2 and dc == 1)):
                return False
        return True
