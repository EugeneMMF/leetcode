class Solution:
    def minDays(self, grid):
        m, n = len(grid), len(grid[0])
        def count_islands():
            visited = [[False]*n for _ in range(m)]
            dirs = [(1,0),(-1,0),(0,1),(0,-1)]
            islands = 0
            for i in range(m):
                for j in range(n):
                    if grid[i][j]==1 and not visited[i][j]:
                        islands += 1
                        stack = [(i,j)]
                        visited[i][j]=True
                        while stack:
                            x,y = stack.pop()
                            for dx,dy in dirs:
                                nx, ny = x+dx, y+dy
                                if 0<=nx<m and 0<=ny<n and grid[nx][ny]==1 and not visited[nx][ny]:
                                    visited[nx][ny]=True
                                    stack.append((nx,ny))
            return islands
        total_ones = sum(cell for row in grid for cell in row)
        if count_islands() != 1:
            return 0
        if total_ones <= 2:
            return total_ones
        disc = {}
        low = {}
        parent = {}
        time = 0
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        found_articulation = False
        def dfs(u):
            nonlocal time, found_articulation
            time += 1
            disc[u] = low[u] = time
            child_count = 0
            x, y = u
            for dx, dy in dirs:
                nx, ny = x+dx, y+dy
                v = (nx, ny)
                if 0<=nx<m and 0<=ny<n and grid[nx][ny]==1:
                    if v not in disc:
                        parent[v] = u
                        child_count += 1
                        dfs(v)
                        low[u] = min(low[u], low[v])
                        if parent.get(u) is None:
                            if child_count > 1:
                                found_articulation = True
                        else:
                            if low[v] >= disc[u]:
                                found_articulation = True
                    elif parent.get(u) != v:
                        low[u] = min(low[u], disc[v])
        start = None
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    start = (i,j)
                    break
            if start:
                break
        dfs(start)
        return 1 if found_articulation else 2
