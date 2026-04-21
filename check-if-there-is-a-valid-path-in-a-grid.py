class Solution:
    def hasValidPath(self, grid):
        m=len(grid);n=len(grid[0])
        dirs=[(-1,0),(1,0),(0,-1),(0,1)]
        conn={1:{(0,-1),(0,1)},2:{(-1,0),(1,0)},3:{(0,-1),(1,0)},4:{(0,1),(1,0)},5:{(0,-1),(-1,0)},6:{(0,1),(-1,0)}}
        from collections import deque
        q=deque()
        q.append((0,0))
        visited=[[False]*n for _ in range(m)]
        visited[0][0]=True
        while q:
            i,j=q.popleft()
            if i==m-1 and j==n-1:
                return True
            for di,dj in dirs:
                ni=i+di;nj=j+dj
                if 0<=ni<m and 0<=nj<n and not visited[ni][nj]:
                    if (di,dj) in conn[grid[i][j]] and (-di,-dj) in conn[grid[ni][nj]]:
                        visited[ni][nj]=True
                        q.append((ni,nj))
        return False
