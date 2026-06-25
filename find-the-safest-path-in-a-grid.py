class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        from collections import deque
        import heapq
        n = len(grid)
        dist = [[10**9]*n for _ in range(n)]
        q = deque()
        for i in range(n):
            for j in range(n):
                if grid[i][j]==1:
                    dist[i][j]=0
                    q.append((i,j))
        dirs=[(1,0),(-1,0),(0,1),(0,-1)]
        while q:
            r,c=q.popleft()
            d=dist[r][c]+1
            for dr,dc in dirs:
                nr,nc=r+dr,c+dc
                if 0<=nr<n and 0<=nc<n and dist[nr][nc]>d:
                    dist[nr][nc]=d
                    q.append((nr,nc))
        best=[[-1]*n for _ in range(n)]
        heap=[(-dist[0][0],0,0)]
        best[0][0]=dist[0][0]
        while heap:
            cap,r,c=heapq.heappop(heap)
            cap=-cap
            if cap<best[r][c]:
                continue
            if r==n-1 and c==n-1:
                return cap
            for dr,dc in dirs:
                nr,nc=r+dr,c+dc
                if 0<=nr<n and 0<=nc<n:
                    newCap=min(cap,dist[nr][nc])
                    if newCap>best[nr][nc]:
                        best[nr][nc]=newCap
                        heapq.heappush(heap,(-newCap,nr,nc))
        return 0