class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        m = len(points)
        n = len(points[0]) if m else 0
        dp = points[0][:]
        for r in range(1, m):
            left = [0] * n
            right = [0] * n
            best = -10**18
            for c in range(n):
                best = max(best - 1, dp[c])
                left[c] = best
            best = -10**18
            for c in range(n - 1, -1, -1):
                best = max(best - 1, dp[c])
                right[c] = best
            dp = [points[r][c] + max(left[c], right[c]) for c in range(n)]
        return max(dp)
