class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m = len(grid1)
        n = len(grid1[0])
        res = 0
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1:
                    stack = [(i, j)]
                    grid2[i][j] = 0
                    is_sub = True
                    while stack:
                        x, y = stack.pop()
                        if grid1[x][y] == 0:
                            is_sub = False
                        for dx, dy in dirs:
                            nx, ny = x + dx, y + dy
                            if 0 <= nx < m and 0 <= ny < n and grid2[nx][ny] == 1:
                                grid2[nx][ny] = 0
                                stack.append((nx, ny))
                    if is_sub:
                        res += 1
        return res
