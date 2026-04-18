class Solution:
    def getMaximumGold(self, grid):
        m, n = len(grid), len(grid[0])
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        def dfs(i,j):
            gold = grid[i][j]
            grid[i][j] = 0
            best = 0
            for di,dj in dirs:
                ni, nj = i+di, j+dj
                if 0 <= ni < m and 0 <= nj < n and grid[ni][nj]:
                    best = max(best, dfs(ni, nj))
            grid[i][j] = gold
            return gold + best
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    ans = max(ans, dfs(i, j))
        return ans
