class Solution:
    def countTriplets(self, nums):
        from typing import List
        MAX = 1 << 16
        full = MAX - 1
        cnt = [0] * MAX
        for v in nums:
            cnt[v] += 1
        sup = cnt[:]
        for b in range(16):
            step = 1 << b
            for mask in range(MAX):
                if not (mask & step):
                    sup[mask] += sup[mask | step]
        pair = [x * x for x in sup]
        for b in range(16):
            step = 1 << b
            for mask in range(MAX):
                if not (mask & step):
                    pair[mask] -= pair[mask | step]
        sub = cnt[:]
        for b in range(16):
            step = 1 << b
            for mask in range(MAX):
                if mask & step:
                    sub[mask] += sub[mask ^ step]
        ans = 0
        for mask in range(MAX):
            comp = full ^ mask
            ans += pair[mask] * sub[comp]
        return ans
