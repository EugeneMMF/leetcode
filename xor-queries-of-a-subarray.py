from typing import List

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        n = len(arr)
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] ^ arr[i]
        res = []
        for l, r in queries:
            res.append(pref[r + 1] ^ pref[l])
        return res
