class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        grid = [[1] * n for _ in range(n)]
        for r, c in mines:
            grid[r][c] = 0

        dp = [[[0] * 4 for _ in range(n)] for _ in range(n)]

        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    dp[r][c][0] = (dp[r - 1][c][0] + 1) if r > 0 else 1
                    dp[r][c][1] = (dp[r][c - 1][1] + 1) if c > 0 else 1

        for r in range(n - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                if grid[r][c] == 1:
                    dp[r][c][2] = (dp[r + 1][c][2] + 1) if r < n - 1 else 1
                    dp[r][c][3] = (dp[r][c + 1][3] + 1) if c < n - 1 else 1

        max_order = 0
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    min_arm = min(dp[r][c])
                    max_order = max(max_order, min_arm)

        return max_order
