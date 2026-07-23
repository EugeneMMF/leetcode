class Solution:
    def countOfPairs(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        req = [0] * n
        for i in range(1, n):
            d = nums[i] - nums[i-1]
            if d > 0:
                req[i] = req[i-1] + d
            else:
                req[i] = req[i-1]
        U0 = min(nums[i] - req[i] for i in range(n))
        if U0 < 0:
            return 0
        t = nums[-1] - req[-1]
        m = n - 1
        L = t - U0
        maxN = t + m + 2
        if L + m + 1 > maxN:
            maxN = L + m + 1
        maxN += 5
        fac = [1] * (maxN)
        for i in range(1, maxN):
            fac[i] = fac[i-1] * i % MOD
        invfac = [1] * (maxN)
        invfac[-1] = pow(fac[-1], MOD-2, MOD)
        for i in range(maxN-2, -1, -1):
            invfac[i] = invfac[i+1] * (i+1) % MOD
        def comb(a, b):
            if b < 0 or b > a or a < 0:
                return 0
            return fac[a] * invfac[b] % MOD * invfac[a-b] % MOD
        ans = comb(t + m + 1, m + 1) - comb(L + m, m + 1)
        ans %= MOD
        return ans
