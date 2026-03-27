class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        max_area = 0

        def dfs(r, c):
            if not (0 <= r < m and 0 <= c < n and grid[r][c] == 1):
                return 0

            grid[r][c] = 0
            current_area = 1

            current_area += dfs(r + 1, c)
            current_area += dfs(r - 1, c)
            current_area += dfs(r, c + 1)
            current_area += dfs(r, c - 1)

            return current_area

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    max_area = max(max_area, dfs(r, c))
        
        return max_area
