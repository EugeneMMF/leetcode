class Solution:
    def matrixBlockSum(self, mat, k):
        m = len(mat)
        n = len(mat[0])
        ps = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            row_sum = 0
            for j in range(n):
                row_sum += mat[i][j]
                ps[i + 1][j + 1] = ps[i][j + 1] + row_sum
        ans = [[0] * n for _ in range(m)]
        for i in range(m):
            r1 = max(0, i - k)
            r2 = min(m - 1, i + k)
            for j in range(n):
                c1 = max(0, j - k)
                c2 = min(n - 1, j + k)
                ans[i][j] = ps[r2 + 1][c2 + 1] - ps[r1][c2 + 1] - ps[r2 + 1][c1] + ps[r1][c1]
        return ans
