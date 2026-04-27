class Solution:
    def numOfWays(self, nums):
        MOD = 10**9 + 7
        n = len(nums)
        fact = [1] * (n + 1)
        inv = [1] * (n + 1)
        for i in range(1, n + 1):
            fact[i] = fact[i - 1] * i % MOD
        inv[n] = pow(fact[n], MOD - 2, MOD)
        for i in range(n, 0, -1):
            inv[i - 1] = inv[i] * i % MOD
        def comb(a, b):
            return fact[a] * inv[b] % MOD * inv[a - b] % MOD
        def dfs(arr):
            if len(arr) <= 1:
                return len(arr), 1
            root = arr[0]
            left = [x for x in arr[1:] if x < root]
            right = [x for x in arr[1:] if x > root]
            lsize, lways = dfs(left)
            rsize, rways = dfs(right)
            ways = comb(lsize + rsize, lsize) * lways % MOD * rways % MOD
            return lsize + rsize + 1, ways
        _, total = dfs(nums)
        return (total - 1) % MOD
