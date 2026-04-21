class Solution:
    def stoneGameIII(self, stoneValue):
        n = len(stoneValue)
        dp = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            best = -10**9
            cur = 0
            for k in range(1, 4):
                if i + k > n:
                    break
                cur += stoneValue[i + k - 1]
                best = max(best, cur - dp[i + k])
            dp[i] = best
        diff = dp[0]
        return "Alice" if diff > 0 else ("Bob" if diff < 0 else "Tie")
