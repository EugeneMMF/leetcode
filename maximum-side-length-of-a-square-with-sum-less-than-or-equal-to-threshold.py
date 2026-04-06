class Solution:
    def maxSideLength(self, mat: list[list[int]], threshold: int) -> int:
        m, n = len(mat), len(mat[0])
        prefix_sum = [[0] * (n + 1) for _ in range(m + 1)]

        for r in range(m):
            for c in range(n):
                prefix_sum[r + 1][c + 1] = mat[r][c] + prefix_sum[r][c + 1] + prefix_sum[r + 1][c] - prefix_sum[r][c]

        def get_square_sum(r, c, k):
            return prefix_sum[r + k][c + k] - prefix_sum[r][c + k] - prefix_sum[r + k][c] + prefix_sum[r][c]

        for k in range(min(m, n), 0, -1):
            for r in range(m - k + 1):
                for c in range(n - k + 1):
                    if get_square_sum(r, c, k) <= threshold:
                        return k
        return 0

