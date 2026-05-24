class Solution:
    def maxTrailingZeros(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        def factor_counts(x):
            c2 = c5 = 0
            while x % 2 == 0:
                c2 += 1
                x //= 2
            while x % 5 == 0:
                c5 += 1
                x //= 5
            return c2, c5

        up2 = [[0]*n for _ in range(m)]
        up5 = [[0]*n for _ in range(m)]
        left2 = [[0]*n for _ in range(m)]
        left5 = [[0]*n for _ in range(m)]
        down2 = [[0]*n for _ in range(m)]
        down5 = [[0]*n for _ in range(m)]
        right2 = [[0]*n for _ in range(m)]
        right5 = [[0]*n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                c2, c5 = factor_counts(grid[i][j])
                up2[i][j] = (up2[i-1][j] if i>0 else 0) + c2
                up5[i][j] = (up5[i-1][j] if i>0 else 0) + c5
                left2[i][j] = (left2[i][j-1] if j>0 else 0) + c2
                left5[i][j] = (left5[i][j-1] if j>0 else 0) + c5

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                c2, c5 = factor_counts(grid[i][j])
                down2[i][j] = (down2[i+1][j] if i<m-1 else 0) + c2
                down5[i][j] = (down5[i+1][j] if i<m-1 else 0) + c5
                right2[i][j] = (right2[i][j+1] if j<n-1 else 0) + c2
                right5[i][j] = (right5[i][j+1] if j<n-1 else 0) + c5

        best = 0
        for i in range(m):
            for j in range(n):
                c2, c5 = factor_counts(grid[i][j])
                # up + left
                t2 = up2[i][j] + left2[i][j] - c2
                t5 = up5[i][j] + left5[i][j] - c5
                best = max(best, min(t2, t5))
                # up + right
                t2 = up2[i][j] + right2[i][j] - c2
                t5 = up5[i][j] + right5[i][j] - c5
                best = max(best, min(t2, t5))
                # down + left
                t2 = down2[i][j] + left2[i][j] - c2
                t5 = down5[i][j] + left5[i][j] - c5
                best = max(best, min(t2, t5))
                # down + right
                t2 = down2[i][j] + right2[i][j] - c2
                t5 = down5[i][j] + right5[i][j] - c5
                best = max(best, min(t2, t5))
        return best
