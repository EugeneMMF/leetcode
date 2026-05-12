from typing import List
class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        sums = set()
        for i in range(m):
            for j in range(n):
                sums.add(grid[i][j])
                max_k = min(i, j, m - 1 - i, n - 1 - j)
                for k in range(1, max_k + 1):
                    total = 0
                    for s in range(k):
                        total += grid[i - k + s][j + s]
                        total += grid[i + s][j + k - s]
                        total += grid[i + k - s][j - s]
                        total += grid[i - s][j - k + s]
                    sums.add(total)
        return sorted(sums, reverse=True)[:3]