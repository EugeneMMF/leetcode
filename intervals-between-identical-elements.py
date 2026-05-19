class Solution:
    def getDistances(self, arr):
        n = len(arr)
        pos = {}
        for i, v in enumerate(arr):
            pos.setdefault(v, []).append(i)
        res = [0] * n
        for indices in pos.values():
            m = len(indices)
            if m == 1:
                continue
            pref = [0] * m
            pref[0] = indices[0]
            for i in range(1, m):
                pref[i] = pref[i - 1] + indices[i]
            total = pref[-1]
            for k, idx in enumerate(indices):
                left = idx * k - (pref[k - 1] if k > 0 else 0)
                right = (total - pref[k]) - idx * (m - k - 1)
                res[idx] = left + right
        return res
