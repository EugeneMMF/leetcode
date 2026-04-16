class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        n, m = len(str1), len(str2)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            a = str1[i - 1]
            row = dp[i]
            prev_row = dp[i - 1]
            for j in range(1, m + 1):
                if a == str2[j - 1]:
                    row[j] = prev_row[j - 1] + 1
                else:
                    row[j] = prev_row[j] if prev_row[j] >= row[j - 1] else row[j - 1]
        i, j = n, m
        res = []
        while i > 0 and j > 0:
            if str1[i - 1] == str2[j - 1]:
                res.append(str1[i - 1])
                i -= 1
                j -= 1
            elif dp[i - 1][j] >= dp[i][j - 1]:
                res.append(str1[i - 1])
                i -= 1
            else:
                res.append(str2[j - 1])
                j -= 1
        while i > 0:
            res.append(str1[i - 1])
            i -= 1
        while j > 0:
            res.append(str2[j - 1])
            j -= 1
        return ''.join(reversed(res))
