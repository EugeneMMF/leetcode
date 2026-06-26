class Solution:
    def countKSubsequencesWithMaxBeauty(self, s: str, k: int) -> int:
        MOD = 10**9 + 7
        freq = [0]*26
        for ch in s:
            freq[ord(ch)-97] += 1
        freqs = [f for f in freq if f>0]
        distinct = len(freqs)
        if k>distinct:
            return 0
        freqs.sort(reverse=True)
        threshold = freqs[k-1]
        greater = sum(1 for f in freqs if f>threshold)
        equal = sum(1 for f in freqs if f==threshold)
        t = k - greater
        prod_greater = 1
        for i in range(greater):
            prod_greater = (prod_greater * freqs[i]) % MOD
        # precompute factorials up to equal
        fact = [1]*(equal+1)
        for i in range(1,equal+1):
            fact[i] = fact[i-1]*i%MOD
        inv_fact = [1]*(equal+1)
        inv_fact[equal] = pow(fact[equal], MOD-2, MOD)
        for i in range(equal,0,-1):
            inv_fact[i-1] = inv_fact[i]*i%MOD
        comb = fact[equal]*inv_fact[t]%MOD*inv_fact[equal-t]%MOD
        ans = prod_greater * comb % MOD
        ans = ans * pow(threshold, t, MOD) % MOD
        return ans