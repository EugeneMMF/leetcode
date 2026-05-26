class Solution:
    def sellingWood(self, m: int, n: int, prices: List[List[int]]) -> int:
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for h, w, p in prices:
            dp[h][w] = max(dp[h][w], p)
        for h in range(1, m + 1):
            for w in range(1, n + 1):
                best = dp[h][w]
                for k in range(1, h // 2 + 1):
                    val = dp[k][w] + dp[h - k][w]
                    if val > best:
                        best = val
                for k in range(1, w // 2 + 1):
                    val = dp[h][k] + dp[h][w - k]
                    if val > best:
                        best = val
                dp[h][w] = best
        return dp[m][n]