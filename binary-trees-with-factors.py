class Solution:
    def numFactoredBinaryTrees(self, arr):
        MOD = 10**9 + 7
        arr.sort()
        s = set(arr)
        dp = {}
        for v in arr:
            total = 1
            for left in arr:
                if left > v:
                    break
                if v % left == 0:
                    right = v // left
                    if right in s:
                        total = (total + dp[left] * dp[right]) % MOD
            dp[v] = total
        return sum(dp.values()) % MOD
