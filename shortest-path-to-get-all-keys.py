from collections import deque
from typing import List

class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        m=len(grid); n=len(grid[0])
        start=None
        total=0
        for i in range(m):
            for j in range(n):
                c=grid[i][j]
                if c=='@':
                    start=(i,j)
                elif 'a'<=c<='f':
                    total+=1
        target=(1<<total)-1
        q=deque()
        q.append((start[0],start[1],0,0))
        visited=set()
        visited.add((start[0],start[1],0))
        dirs=[(1,0),(-1,0),(0,1),(0,-1)]
        while q:
            x,y,mask,steps=q.popleft()
            if mask==target:
                return steps
            for dx,dy in dirs:
                nx,ny=x+dx,y+dy
                if 0<=nx<m and 0<=ny<n:
                    cell=grid[nx][ny]
                    if cell=='#':
                        continue
                    nmask=mask
                    if 'a'<=cell<='f':
                        nmask=mask| (1<<(ord(cell)-ord('a')))
                    if 'A'<=cell<='F' and not (mask & (1<<(ord(cell)-ord('A')))):
                        continue
                    if (nx,ny,nmask) not in visited:
                        visited.add((nx,ny,nmask))
                        q.append((nx,ny,nmask,steps+1))
        return -1
