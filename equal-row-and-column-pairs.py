class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        row_counts = {}
        for r in grid:
            t = tuple(r)
            row_counts[t] = row_counts.get(t, 0) + 1
        ans = 0
        for c in range(n):
            col = tuple(grid[i][c] for i in range(n))
            ans += row_counts.get(col, 0)
        return ans
