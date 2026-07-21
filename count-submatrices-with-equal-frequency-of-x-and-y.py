class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0]) if n else 0
        sumX = [[0]*m for _ in range(n)]
        sumY = [[0]*m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                valX = 1 if grid[i][j]=='X' else 0
                valY = 1 if grid[i][j]=='Y' else 0
                sumX[i][j] = valX + (sumX[i-1][j] if i>0 else 0) + (sumX[i][j-1] if j>0 else 0) - (sumX[i-1][j-1] if i>0 and j>0 else 0)
                sumY[i][j] = valY + (sumY[i-1][j] if i>0 else 0) + (sumY[i][j-1] if j>0 else 0) - (sumY[i-1][j-1] if i>0 and j>0 else 0)
        ans = 0
        for i in range(n):
            for j in range(m):
                if sumX[i][j] == sumY[i][j] and sumX[i][j] >= 1:
                    ans += 1
        return ans