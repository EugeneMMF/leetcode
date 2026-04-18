class Solution:
    def minimumMoves(self, grid):
        from collections import deque
        n = len(grid)
        start = (0, 0, 0)
        target = (n - 1, n - 2, 0)
        q = deque([start])
        visited = {start}
        steps = 0
        while q:
            for _ in range(len(q)):
                r, c, o = q.popleft()
                if (r, c, o) == target:
                    return steps
                if o == 0:
                    if c + 2 < n and grid[r][c + 2] == 0:
                        ns = (r, c + 1, 0)
                        if ns not in visited:
                            visited.add(ns)
                            q.append(ns)
                    if r + 1 < n and grid[r + 1][c] == 0 and grid[r + 1][c + 1] == 0:
                        ns = (r + 1, c, 0)
                        if ns not in visited:
                            visited.add(ns)
                            q.append(ns)
                        ns = (r, c, 1)
                        if ns not in visited:
                            visited.add(ns)
                            q.append(ns)
                else:
                    if r + 2 < n and grid[r + 2][c] == 0:
                        ns = (r + 1, c, 1)
                        if ns not in visited:
                            visited.add(ns)
                            q.append(ns)
                    if c + 1 < n and grid[r][c + 1] == 0 and grid[r + 1][c + 1] == 0:
                        ns = (r, c + 1, 1)
                        if ns not in visited:
                            visited.add(ns)
                            q.append(ns)
                        ns = (r, c, 0)
                        if ns not in visited:
                            visited.add(ns)
                            q.append(ns)
            steps += 1
        return -1
