from collections import deque

class Solution:
    def shortestPath(self, grid: list[list[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        if k >= m + n - 2:
            return m + n - 2

        queue = deque([(0, 0, k, 0)])
        visited = set([(0, 0, k)])

        while queue:
            r, c, obstacles, steps = queue.popleft()

            if r == m - 1 and c == n - 1:
                return steps

            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc

                if 0 <= nr < m and 0 <= nc < n:
                    new_obstacles = obstacles - grid[nr][nc]
                    if new_obstacles >= 0 and (nr, nc, new_obstacles) not in visited:
                        visited.add((nr, nc, new_obstacles))
                        queue.append((nr, nc, new_obstacles, steps + 1))

        return -1

