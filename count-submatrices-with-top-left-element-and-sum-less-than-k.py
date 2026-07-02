class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0]) if m else 0
        pref = [[0]*n for _ in range(m)]
        count = 0
        for i in range(m):
            row_sum = 0
            for j in range(n):
                row_sum += grid[i][j]
                pref[i][j] = row_sum
                if i > 0:
                    pref[i][j] += pref[i-1][j]
                if pref[i][j] <= k:
                    count += 1
        return count