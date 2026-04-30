from typing import List

class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        MOD = 10**9 + 7
        freq = {}
        res = 0
        powers = [1 << i for i in range(22)]
        for v in deliciousness:
            for p in powers:
                need = p - v
                if need in freq:
                    res = (res + freq[need]) % MOD
            freq[v] = freq.get(v, 0) + 1
        return res
