class Solution:
    def minimumBeautifulSubstrings(self, s: str) -> int:
        n = len(s)
        max_val = (1 << n) - 1
        powers = set()
        val = 1
        while val <= max_val:
            powers.add(bin(val)[2:])
            val *= 5
        INF = 10**9
        dp = [INF] * (n + 1)
        dp[0] = 0
        for i in range(1, n + 1):
            for j in range(i):
                sub = s[j:i]
                if sub[0] == '0':
                    continue
                if sub in powers:
                    dp[i] = min(dp[i], dp[j] + 1)
        return dp[n] if dp[n] != INF else -1