class Solution:
    def rotateGrid(self, grid, k):
        m, n = len(grid), len(grid[0])
        layers = min(m, n) // 2
        for l in range(layers):
            top, left = l, l
            bottom, right = m - 1 - l, n - 1 - l
            pos = []
            for c in range(left, right + 1):
                pos.append((top, c))
            for r in range(top + 1, bottom):
                pos.append((r, right))
            for c in range(right, left - 1, -1):
                pos.append((bottom, c))
            for r in range(bottom - 1, top, -1):
                pos.append((r, left))
            vals = [grid[r][c] for r, c in pos]
            lsize = len(vals)
            shift = k % lsize
            if shift:
                rotated = vals[shift:] + vals[:shift]
                for (r, c), v in zip(pos, rotated):
                    grid[r][c] = v
        return grid
