class Solution:
    def regionsBySlashes(self, grid: list[str]) -> int:
        n = len(grid)
        dot = [[0] * (3 * n) for _ in range(3 * n)]
        for r in range(n):
            for c in range(n):
                if grid[r][c] == '/':
                    dot[3 * r + 0][3 * c + 2] = 1
                    dot[3 * r + 1][3 * c + 1] = 1
                    dot[3 * r + 2][3 * c + 0] = 1
                elif grid[r][c] == '\\':
                    dot[3 * r + 0][3 * c + 0] = 1
                    dot[3 * r + 1][3 * c + 1] = 1
                    dot[3 * r + 2][3 * c + 2] = 1

        count = 0
        for r in range(3 * n):
            for c in range(3 * n):
                if dot[r][c] == 0:
                    count += 1
                    stack = [(r, c)]
                    dot[r][c] = 1
                    while stack:
                        row, col = stack.pop()
                        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                            nr, nc = row + dr, col + dc
                            if 0 <= nr < 3 * n and 0 <= nc < 3 * n and dot[nr][nc] == 0:
                                dot[nr][nc] = 1
                                stack.append((nr, nc))
        return count

