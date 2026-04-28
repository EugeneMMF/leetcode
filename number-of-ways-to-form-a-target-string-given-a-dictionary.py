class Solution:
    def numWays(self, words, target):
        MOD = 10**9 + 7
        m = len(words[0])
        n = len(target)
        cnt = [[0] * 26 for _ in range(m)]
        for w in words:
            for i, ch in enumerate(w):
                cnt[i][ord(ch) - 97] += 1
        dp = [0] * (n + 1)
        dp[0] = 1
        for pos in range(m):
            ch_idx = ord(target[-1]) - 97
            for t in range(n, 0, -1):
                dp[t] = (dp[t] + dp[t-1] * cnt[pos][ord(target[t-1]) - 97]) % MOD
        return dp[n]
