class Solution:
    def minimumEffortPath(self, heights):
        import heapq
        m, n = len(heights), len(heights[0])
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        effort = [[float('inf')]*n for _ in range(m)]
        effort[0][0] = 0
        heap = [(0,0,0)]
        while heap:
            e, x, y = heapq.heappop(heap)
            if e != effort[x][y]:
                continue
            if x == m-1 and y == n-1:
                return e
            for dx, dy in dirs:
                nx, ny = x+dx, y+dy
                if 0 <= nx < m and 0 <= ny < n:
                    ne = max(e, abs(heights[x][y]-heights[nx][ny]))
                    if ne < effort[nx][ny]:
                        effort[nx][ny] = ne
                        heapq.heappush(heap, (ne, nx, ny))