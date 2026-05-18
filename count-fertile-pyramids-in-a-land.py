class Solution:
    def countPyramids(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0]) if m else 0
        dp_up = [[0]*n for _ in range(m)]
        dp_down = [[0]*n for _ in range(m)]
        for i in range(m-1, -1, -1):
            for j in range(n):
                if grid[i][j]==1:
                    if i+1<m and j-1>=0 and j+1<n:
                        dp_up[i][j] = 1 + min(dp_up[i+1][j-1], dp_up[i+1][j], dp_up[i+1][j+1])
                    else:
                        dp_up[i][j] = 1
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    if i-1>=0 and j-1>=0 and j+1<n:
                        dp_down[i][j] = 1 + min(dp_down[i-1][j-1], dp_down[i-1][j], dp_down[i-1][j+1])
                    else:
                        dp_down[i][j] = 1
        total = 0
        for i in range(m):
            for j in range(n):
                if dp_up[i][j]>1:
                    total += dp_up[i][j]-1
                if dp_down[i][j]>1:
                    total += dp_down[i][j]-1
        return total