class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = 10**9 + 7
        dp = [0] * (target + 1)
        dp[0] = 1
        for _ in range(n):
            ndp = [0] * (target + 1)
            for t in range(1, target + 1):
                total = 0
                for face in range(1, k + 1):
                    if t - face >= 0:
                        total += dp[t - face]
                ndp[t] = total % MOD
            dp = ndp
        return dp[target]
