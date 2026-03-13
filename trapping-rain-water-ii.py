import heapq

class Solution:
    def trapRainWater(self, heightMap: list[list[int]]) -> int:
        m = len(heightMap)
        n = len(heightMap[0])

        min_heap = []
        visited = [[False for _ in range(n)] for _ in range(m)]

        for c in range(n):
            heapq.heappush(min_heap, (heightMap[0][c], 0, c))
            visited[0][c] = True
            heapq.heappush(min_heap, (heightMap[m-1][c], m-1, c))
            visited[m-1][c] = True
        
        for r in range(1, m-1):
            heapq.heappush(min_heap, (heightMap[r][0], r, 0))
            visited[r][0] = True
            heapq.heappush(min_heap, (heightMap[r][n-1], r, n-1))
            visited[r][n-1] = True

        total_water = 0
        max_level = 0

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while min_heap:
            height, r, c = heapq.heappop(min_heap)

            max_level = max(max_level, height)

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc]:
                    visited[nr][nc] = True
                    
                    if heightMap[nr][nc] < max_level:
                        total_water += max_level - heightMap[nr][nc]
                    
                    heapq.heappush(min_heap, (max(heightMap[nr][nc], max_level), nr, nc))
        
        return total_water
