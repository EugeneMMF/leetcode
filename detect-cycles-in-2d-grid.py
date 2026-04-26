class Solution:
    def containsCycle(self, grid):
        m=len(grid); n=len(grid[0])
        visited=[[False]*n for _ in range(m)]
        dirs=[(1,0),(-1,0),(0,1),(0,-1)]
        for i in range(m):
            for j in range(n):
                if not visited[i][j]:
                    stack=[(i,j,-1,-1)]
                    visited[i][j]=True
                    while stack:
                        x,y,px,py=stack.pop()
                        for dx,dy in dirs:
                            nx,ny=x+dx,y+dy
                            if 0<=nx<m and 0<=ny<n and grid[nx][ny]==grid[x][y]:
                                if not visited[nx][ny]:
                                    visited[nx][ny]=True
                                    stack.append((nx,ny,x,y))
                                elif nx!=px or ny!=py:
                                    return True
        return False
