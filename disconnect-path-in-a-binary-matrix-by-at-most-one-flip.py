from typing import List
from collections import deque

class Solution:
    def isPossibleToCutPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        def has_path():
            if grid[0][0] == 0 or grid[m-1][n-1] == 0:
                return False
            vis = [[False]*n for _ in range(m)]
            q = deque([(0,0)])
            vis[0][0] = True
            while q:
                i,j = q.popleft()
                if (i,j) == (m-1,n-1):
                    return True
                for di,dj in ((1,0),(0,1)):
                    ni,nj = i+di,j+dj
                    if 0<=ni<m and 0<=nj<n and grid[ni][nj]==1 and not vis[ni][nj]:
                        vis[ni][nj] = True
                        q.append((ni,nj))
            return False
        if not has_path():
            return True
        p1 = 1000000007
        p2 = 1000000009
        ways_start1 = [[0]*n for _ in range(m)]
        ways_start2 = [[0]*n for _ in range(m)]
        ways_end1 = [[0]*n for _ in range(m)]
        ways_end2 = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    continue
                if i == 0 and j == 0:
                    ways_start1[i][j] = 1
                    ways_start2[i][j] = 1
                else:
                    v1 = 0
                    v2 = 0
                    if i > 0:
                        v1 += ways_start1[i-1][j]
                        v2 += ways_start2[i-1][j]
                    if j > 0:
                        v1 += ways_start1[i][j-1]
                        v2 += ways_start2[i][j-1]
                    ways_start1[i][j] = v1 % p1
                    ways_start2[i][j] = v2 % p2
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if grid[i][j] == 0:
                    continue
                if i == m-1 and j == n-1:
                    ways_end1[i][j] = 1
                    ways_end2[i][j] = 1
                else:
                    v1 = 0
                    v2 = 0
                    if i < m-1:
                        v1 += ways_end1[i+1][j]
                        v2 += ways_end2[i+1][j]
                    if j < n-1:
                        v1 += ways_end1[i][j+1]
                        v2 += ways_end2[i][j+1]
                    ways_end1[i][j] = v1 % p1
                    ways_end2[i][j] = v2 % p2
        total1 = ways_start1[m-1][n-1]
        total2 = ways_start2[m-1][n-1]
        for i in range(m):
            for j in range(n):
                if (i==0 and j==0) or (i==m-1 and j==n-1):
                    continue
                if grid[i][j] != 1:
                    continue
                if ways_start1[i][j]==0 or ways_end1[i][j]==0:
                    continue
                if (ways_start1[i][j]*ways_end1[i][j])%p1==total1 and (ways_start2[i][j]*ways_end2[i][j])%p2==total2:
                    return True
        return False