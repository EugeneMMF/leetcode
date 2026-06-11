class Solution:
    def waysToReachTarget(self, target: int, types: List[List[int]]) -> int:
        MOD = 10**9 + 7
        dp = [0] * (target + 1)
        dp[0] = 1
        for count, mark in types:
            newdp = [0] * (target + 1)
            for r in range(mark):
                window = 0
                for k, j in enumerate(range(r, target + 1, mark)):
                    window = (window + dp[j]) % MOD
                    if k > count:
                        window = (window - dp[j - (count + 1) * mark]) % MOD
                    newdp[j] = window
            dp = newdp
        return dp[target] % MOD