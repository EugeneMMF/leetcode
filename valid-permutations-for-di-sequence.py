class Solution:
    def numPermsDISequence(self, s: str) -> int:
        MOD = 10**9 + 7
        n = len(s)
        dp = [1]
        for i in range(1, n + 1):
            ndp = [0] * (i + 1)
            if s[i - 1] == 'I':
                cur = 0
                for j in range(i + 1):
                    ndp[j] = cur
                    if j < i:
                        cur = (cur + dp[j]) % MOD
            else:
                cur = 0
                for j in range(i, -1, -1):
                    ndp[j] = cur
                    if j > 0:
                        cur = (cur + dp[j - 1]) % MOD
            dp = ndp
        return sum(dp) % MOD
