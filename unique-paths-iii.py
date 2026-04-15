from typing import List

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m=len(grid); n=len(grid[0])
        total=0
        sx=sy=ex=ey=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]!=-1:
                    total+=1
                if grid[i][j]==1:
                    sx,sy=i,j
                elif grid[i][j]==2:
                    ex,ey=i,j
        self.res=0
        def dfs(x,y,remain):
            if x==ex and y==ey:
                if remain==0:
                    self.res+=1
                return
            temp=grid[x][y]
            grid[x][y]=-1
            for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                nx,ny=x+dx,y+dy
                if 0<=nx<m and 0<=ny<n and grid[nx][ny]!=-1:
                    dfs(nx,ny,remain-1)
            grid[x][y]=temp
        dfs(sx,sy,total-1)
        return self.res
