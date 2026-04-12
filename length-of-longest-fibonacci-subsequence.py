class Solution:
    def lenLongestFibSubseq(self, arr):
        index = {x: i for i, x in enumerate(arr)}
        n = len(arr)
        dp = [[2] * n for _ in range(n)]
        best = 0
        for j in range(n):
            for i in range(j):
                need = arr[j] - arr[i]
                k = index.get(need)
                if k is not None and k < i:
                    dp[i][j] = dp[k][i] + 1
                    if dp[i][j] > best:
                        best = dp[i][j]
        return best if best >= 3 else 0
