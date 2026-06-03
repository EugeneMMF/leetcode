class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        mod = 10**9 + 7
        powers = []
        i = 0
        while n:
            if n & 1:
                powers.append(1 << i)
            n >>= 1
            i += 1
        m = len(powers)
        pref = [0] * m
        pref[0] = powers[0] % mod
        for idx in range(1, m):
            pref[idx] = pref[idx - 1] * powers[idx] % mod
        res = []
        for left, right in queries:
            if left == 0:
                prod = pref[right]
            else:
                prod = pref[right] * pow(pref[left - 1], mod - 2, mod) % mod
            res.append(prod)
        return res
