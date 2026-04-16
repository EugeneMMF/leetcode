class Solution:
    def colorBorder(self, grid, row, col, color):
        m, n = len(grid), len(grid[0])
        orig = grid[row][col]
        visited = [[False]*n for _ in range(m)]
        stack = [(row, col)]
        visited[row][col] = True
        borders = []
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        while stack:
            r, c = stack.pop()
            is_border = False
            for dr, dc in dirs:
                nr, nc = r+dr, c+dc
                if nr<0 or nr>=m or nc<0 or nc>=n:
                    is_border = True
                elif grid[nr][nc] != orig:
                    is_border = True
                else:
                    if not visited[nr][nc]:
                        visited[nr][nc] = True
                        stack.append((nr, nc))
            if is_border:
                borders.append((r, c))
        for r, c in borders:
            grid[r][c] = color
        return grid
