class Solution:
    def possibleToStamp(self, grid, stampHeight, stampWidth):
        m = len(grid)
        n = len(grid[0]) if m else 0
        if stampHeight > m or stampWidth > n:
            for r in range(m):
                for c in range(n):
                    if grid[r][c] == 0:
                        return False
            return True
        ps = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            row_sum = 0
            for j in range(n):
                row_sum += grid[i][j]
                ps[i + 1][j + 1] = ps[i][j + 1] + row_sum
        diff = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m - stampHeight + 1):
            for j in range(n - stampWidth + 1):
                r1, c1 = i, j
                r2, c2 = i + stampHeight - 1, j + stampWidth - 1
                total_ones = ps[r2 + 1][c2 + 1] - ps[r1][c2 + 1] - ps[r2 + 1][c1] + ps[r1][c1]
                if total_ones == 0:
                    diff[r1][c1] += 1
                    diff[r1][c2 + 1] -= 1
                    diff[r2 + 1][c1] -= 1
                    diff[r2 + 1][c2 + 1] += 1
        for i in range(m):
            for j in range(1, n):
                diff[i][j] += diff[i][j - 1]
        for j in range(n):
            for i in range(1, m):
                diff[i][j] += diff[i - 1][j]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and diff[i][j] == 0:
                    return False
        return True