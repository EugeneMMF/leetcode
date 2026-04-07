from collections import deque

class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        dist = [[float('inf')] * n for _ in range(m)]

        dq = deque()

        dist[0][0] = 0
        dq.appendleft((0, 0, 0))

        dr = [0, 0, 1, -1] 
        dc = [1, -1, 0, 0] 

        while dq:
            cost, r, c = dq.popleft()

            if cost > dist[r][c]:
                continue

            for i in range(4):
                nr, nc = r + dr[i], c + dc[i]

                if 0 <= nr < m and 0 <= nc < n:
                    move_cost = 0 if grid[r][c] == (i + 1) else 1
                    
                    new_total_cost = cost + move_cost

                    if new_total_cost < dist[nr][nc]:
                        dist[nr][nc] = new_total_cost
                        if move_cost == 0:
                            dq.appendleft((new_total_cost, nr, nc))
                        else:
                            dq.append((new_total_cost, nr, nc))

        return dist[m - 1][n - 1]
