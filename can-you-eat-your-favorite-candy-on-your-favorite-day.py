class Solution:
    def canEat(self, candiesCount: List[int], queries: List[List[int]]) -> List[bool]:
        pref = [0]
        for c in candiesCount:
            pref.append(pref[-1] + c)
        res = []
        for t, d, cap in queries:
            before = pref[t]
            after = pref[t + 1]
            lower = max(d + 1, before + 1)
            upper = min((d + 1) * cap, after)
            res.append(lower <= upper)
        return res
