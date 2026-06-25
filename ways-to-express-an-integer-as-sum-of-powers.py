class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        mod = 10**9 + 7
        powers = []
        i = 1
        while True:
            val = i**x
            if val > n:
                break
            powers.append(val)
            i += 1
        dp = [0]*(n+1)
        dp[0] = 1
        for p in powers:
            for s in range(n, p-1, -1):
                dp[s] = (dp[s] + dp[s-p]) % mod
        return dp[n]