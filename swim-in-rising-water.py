import heapq
import math

class Solution:
    def swimInWater(self, grid: list[list[int]]) -> int:
        n = len(grid)
        
        dist = [[math.inf] * n for _ in range(n)]
        
        pq = [(grid[0][0], 0, 0)]
        dist[0][0] = grid[0][0]
        
        dr = [-1, 1, 0, 0]
        dc = [0, 0, -1, 1]
        
        while pq:
            current_max_elevation, r, c = heapq.heappop(pq)
            
            if current_max_elevation > dist[r][c]:
                continue
            
            if r == n - 1 and c == n - 1:
                return current_max_elevation
            
            for i in range(4):
                nr, nc = r + dr[i], c + dc[i]
                
                if 0 <= nr < n and 0 <= nc < n:
                    new_max_elevation = max(current_max_elevation, grid[nr][nc])
                    
                    if new_max_elevation < dist[nr][nc]:
                        dist[nr][nc] = new_max_elevation
                        heapq.heappush(pq, (new_max_elevation, nr, nc))
        
        return -1