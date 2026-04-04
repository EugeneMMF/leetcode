class Solution:
    def numEnclaves(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        def dfs(r, c):
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == 0:
                return
            
            grid[r][c] = 0

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for c in range(n):
            if grid[0][c] == 1:
                dfs(0, c)
            if grid[m - 1][c] == 1:
                dfs(m - 1, c)
        
        for r in range(1, m - 1):
            if grid[r][0] == 1:
                dfs(r, 0)
            if grid[r][n - 1] == 1:
                dfs(r, n - 1)

        enclaves_count = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    enclaves_count += 1
        
        return enclaves_count
