class Solution:
    def canMouseWin(self, grid, catJump, mouseJump):
        rows, cols = len(grid), len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 'M':
                    mouse_start = (r, c)
                elif grid[r][c] == 'C':
                    cat_start = (r, c)
                elif grid[r][c] == 'F':
                    food = (r, c)
        max_turns = rows * cols * 2
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        from functools import lru_cache
        def moves(pos, jump):
            r, c = pos
            res = [pos]
            for dr, dc in dirs:
                nr, nc = r, c
                for _ in range(jump):
                    nr += dr
                    nc += dc
                    if not (0 <= nr < rows and 0 <= nc < cols) or grid[nr][nc] == '#':
                        break
                    res.append((nr, nc))
            return res
        @lru_cache(None)
        def dfs(mouse, cat, turn):
            if turn >= max_turns:
                return False
            if mouse == cat:
                return False
            if mouse == food:
                return True
            if cat == food:
                return False
            player = turn % 2
            if player == 0:
                for nmouse in moves(mouse, mouseJump):
                    if dfs(nmouse, cat, turn+1):
                        return True
                return False
            else:
                for ncat in moves(cat, catJump):
                    if not dfs(mouse, ncat, turn+1):
                        return False
                return True
        return dfs(mouse_start, cat_start, 0)
