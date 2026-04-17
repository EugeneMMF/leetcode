from typing import List

class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        n = len(s)
        pref = [0] * (n + 1)
        for i, ch in enumerate(s):
            pref[i + 1] = pref[i] ^ (1 << (ord(ch) - 97))
        res = []
        for l, r, k in queries:
            mask = pref[r + 1] ^ pref[l]
            odd = mask.bit_count()
            odd_needed = (r - l + 1) & 1
            need = 0 if odd <= odd_needed else (odd - odd_needed) // 2
            res.append(need <= k)
        return res
