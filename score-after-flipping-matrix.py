class Solution:
    def matrixScore(self, grid):
        m=len(grid)
        n=len(grid[0])
        for i in range(m):
            if grid[i][0]==0:
                for j in range(n):
                    grid[i][j]^=1
        total=0
        for j in range(n):
            cnt=0
            for i in range(m):
                cnt+=grid[i][j]
            ones=cnt if cnt>=m-cnt else m-cnt
            total+=ones*(1<<(n-1-j))
        return total
