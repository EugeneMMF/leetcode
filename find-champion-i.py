from typing import List

class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        n = len(grid)
        candidate = 0
        for i in range(1, n):
            if grid[candidate][i] == 1:
                continue
            candidate = i
        return candidate
