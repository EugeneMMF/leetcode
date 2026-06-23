class Solution:
    def differenceOfDistinctValues(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        leftAbove = [[0]*n for _ in range(m)]
        rightBelow = [[0]*n for _ in range(m)]
        diagonals = {}
        for r in range(m):
            for c in range(n):
                d = r - c
                diagonals.setdefault(d, []).append((r, c))
        for cells in diagonals.values():
            cells.sort()
            seen = set()
            for r, c in cells:
                leftAbove[r][c] = len(seen)
                seen.add(grid[r][c])
            seen.clear()
            for r, c in reversed(cells):
                rightBelow[r][c] = len(seen)
                seen.add(grid[r][c])
        ans = [[abs(leftAbove[r][c] - rightBelow[r][c]) for c in range(n)] for r in range(m)]
        return ans
