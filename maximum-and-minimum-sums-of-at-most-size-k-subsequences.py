class Solution:
    def minMaxSums(self, nums: List[int], k: int) -> int:
        mod = 10**9+7
        n = len(nums)
        nums.sort()
        fact = [1]*(n+1)
        for i in range(1,n+1):
            fact[i] = fact[i-1]*i%mod
        invfact = [1]*(n+1)
        invfact[n] = pow(fact[n], mod-2, mod)
        for i in range(n,0,-1):
            invfact[i-1] = invfact[i]*i%mod
        def comb(nc, r):
            if r<0 or r>nc:
                return 0
            return fact[nc]*invfact[r]%mod*invfact[nc-r]%mod
        res = 0
        for i, val in enumerate(nums):
            m_suffix = n - i - 1
            cnt_min = 0
            max_t = min(k-1, m_suffix)
            for t in range(max_t+1):
                cnt_min = (cnt_min + comb(m_suffix, t))%mod
            m_prefix = i
            cnt_max = 0
            max_t = min(k-1, m_prefix)
            for t in range(max_t+1):
                cnt_max = (cnt_max + comb(m_prefix, t))%mod
            res = (res + val*(cnt_min+cnt_max))%mod
        return res