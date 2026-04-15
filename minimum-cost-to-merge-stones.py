from typing import List

class Solution:
    def mergeStones(self, stones: List[int], k: int) -> int:
        n = len(stones)
        if (n - 1) % (k - 1):
            return -1
        pre = [0]
        for s in stones:
            pre.append(pre[-1] + s)
        def range_sum(i, j):
            return pre[j + 1] - pre[i]
        INF = 10 ** 9
        dp = [[0] * n for _ in range(n)]
        for length in range(2, n + 1):
            for i in range(0, n - length + 1):
                j = i + length - 1
                best = INF
                m = i
                while m < j:
                    best = min(best, dp[i][m] + dp[m + 1][j])
                    m += k - 1
                dp[i][j] = best
                if (length - 1) % (k - 1) == 0:
                    dp[i][j] += range_sum(i, j)
        return dp[0][n - 1]
