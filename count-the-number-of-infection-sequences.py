class Solution:
    def numberOfSequence(self, n: int, sick: list[int]) -> int:
        mod = 1000000007
        left = sick[0]
        right = n - 1 - sick[-1]
        internal_segments = []
        for i in range(1, len(sick)):
            seg_len = sick[i] - sick[i - 1] - 1
            if seg_len > 0:
                internal_segments.append(seg_len)
        total_uninfected = left + right + sum(internal_segments)
        fact = [1] * (total_uninfected + 1)
        for i in range(1, total_uninfected + 1):
            fact[i] = fact[i - 1] * i % mod
        inv_fact = [1] * (total_uninfected + 1)
        inv_fact[total_uninfected] = pow(fact[total_uninfected], mod - 2, mod)
        for i in range(total_uninfected, 0, -1):
            inv_fact[i - 1] = inv_fact[i] * i % mod
        ways = 1
        for seg_len in internal_segments:
            ways = ways * pow(2, seg_len - 1, mod) % mod
        res = fact[total_uninfected]
        for seg_len in internal_segments:
            res = res * inv_fact[seg_len] % mod
        res = res * inv_fact[left] % mod if left > 0 else res
        res = res * inv_fact[right] % mod if right > 0 else res
        res = res * ways % mod
        return res