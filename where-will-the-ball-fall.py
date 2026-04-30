from typing import List

class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m = len(grid)
        n = len(grid[0])
        result = [-1] * n
        for start in range(n):
            col = start
            stuck = False
            for row in range(m):
                direction = grid[row][col]
                next_col = col + direction
                if next_col < 0 or next_col >= n or grid[row][next_col] != direction:
                    stuck = True
                    break
                col = next_col
            if not stuck:
                result[start] = col
        return result
