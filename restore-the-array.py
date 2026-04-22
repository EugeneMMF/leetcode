class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        mod = 1000000007
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1
        max_len = len(str(k))
        for i in range(1, n + 1):
            num = 0
            power = 1
            for l in range(1, min(max_len, i) + 1):
                j = i - l
                if s[j] == '0':
                    continue
                num = int(s[j:i])
                if num > k:
                    continue
                dp[i] = (dp[i] + dp[j]) % mod
        return dp[n]
