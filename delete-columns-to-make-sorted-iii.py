class Solution:
    def minDeletionSize(self, strs):
        n = len(strs)
        m = len(strs[0])
        dp = [1] * m
        for j in range(m):
            for i in range(j):
                ok = True
                for row in strs:
                    if row[i] > row[j]:
                        ok = False
                        break
                if ok and dp[i] + 1 > dp[j]:
                    dp[j] = dp[i] + 1
        return m - max(dp)
