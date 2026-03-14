import collections

class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        m = len(heights)
        n = len(heights[0])

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        pacific_q = collections.deque()
        pacific_can_reach = [[False for _ in range(n)] for _ in range(m)]

        for r in range(m):
            pacific_q.append((r, 0))
            pacific_can_reach[r][0] = True
        for c in range(1, n):
            pacific_q.append((0, c))
            pacific_can_reach[0][c] = True

        atlantic_q = collections.deque()
        atlantic_can_reach = [[False for _ in range(n)] for _ in range(m)]

        for r in range(m):
            atlantic_q.append((r, n - 1))
            atlantic_can_reach[r][n - 1] = True
        for c in range(n - 1):
            atlantic_q.append((m - 1, c))
            atlantic_can_reach[m - 1][c] = True

        def run_bfs(q_initial, can_reach_grid):
            q = q_initial
            while q:
                r, c = q.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < m and 0 <= nc < n:
                        if not can_reach_grid[nr][nc] and heights[nr][nc] >= heights[r][c]:
                            can_reach_grid[nr][nc] = True
                            q.append((nr, nc))
        
        run_bfs(pacific_q, pacific_can_reach)
        run_bfs(atlantic_q, atlantic_can_reach)

        result = []
        for r in range(m):
            for c in range(n):
                if pacific_can_reach[r][c] and atlantic_can_reach[r][c]:
                    result.append([r, c])
        
        return result
