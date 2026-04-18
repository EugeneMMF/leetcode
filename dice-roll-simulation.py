class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        MOD = 10**9 + 7
        maxR = max(rollMax)
        dp = [[[0] * (maxR + 1) for _ in range(6)] for _ in range(n + 1)]
        for f in range(6):
            dp[1][f][1] = 1
        for i in range(1, n):
            for f in range(6):
                limit = rollMax[f]
                for c in range(1, limit + 1):
                    cur = dp[i][f][c]
                    if not cur:
                        continue
                    for g in range(6):
                        if g == f:
                            if c < rollMax[f]:
                                dp[i + 1][g][c + 1] = (dp[i + 1][g][c + 1] + cur) % MOD
                        else:
                            dp[i + 1][g][1] = (dp[i + 1][g][1] + cur) % MOD
        ans = 0
        for f in range(6):
            for c in range(1, rollMax[f] + 1):
                ans = (ans + dp[n][f][c]) % MOD
        return ans
