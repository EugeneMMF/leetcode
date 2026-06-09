class Solution:
    def countAnagrams(self, s: str) -> int:
        words = s.split(' ')
        max_len = max(len(w) for w in words)
        mod = 10**9+7
        fact = [1] * (max_len + 1)
        for i in range(1, max_len + 1):
            fact[i] = fact[i - 1] * i % mod
        invfact = [1] * (max_len + 1)
        invfact[max_len] = pow(fact[max_len], mod - 2, mod)
        for i in range(max_len, 0, -1):
            invfact[i - 1] = invfact[i] * i % mod
        res = 1
        for w in words:
            freq = [0] * 26
            for ch in w:
                freq[ord(ch) - 97] += 1
            perm = fact[len(w)]
            for c in freq:
                if c > 1:
                    perm = perm * invfact[c] % mod
            res = res * perm % mod
        return res
