from typing import List

class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0]) if m else 0
        rowOnes = [0] * m
        colOnes = [0] * n
        for i in range(m):
            row = grid[i]
            cnt = sum(row)
            rowOnes[i] = cnt
            for j, val in enumerate(row):
                if val:
                    colOnes[j] += 1
        total = m + n
        diff = [[0] * n for _ in range(m)]
        for i in range(m):
            r = rowOnes[i]
            for j in range(n):
                diff[i][j] = 2 * r + 2 * colOnes[j] - total
        return diff
