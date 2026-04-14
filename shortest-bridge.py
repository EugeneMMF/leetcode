class Solution:
    def shortestBridge(self, grid):
        n = len(grid)
        from collections import deque
        visited = [[False]*n for _ in range(n)]
        q = deque()
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        def dfs(i,j):
            if i<0 or i>=n or j<0 or j>=n or visited[i][j] or grid[i][j]==0:
                return
            visited[i][j]=True
            q.append((i,j))
            for di,dj in dirs:
                dfs(i+di,j+dj)
        found=False
        for i in range(n):
            if found: break
            for j in range(n):
                if grid[i][j]==1:
                    dfs(i,j)
                    found=True
                    break
        steps=0
        while q:
            for _ in range(len(q)):
                i,j = q.popleft()
                for di,dj in dirs:
                    ni,nj = i+di,j+dj
                    if 0<=ni<n and 0<=nj<n and not visited[ni][nj]:
                        if grid[ni][nj]==1:
                            return steps
                        visited[ni][nj]=True
                        q.append((ni,nj))
            steps+=1
