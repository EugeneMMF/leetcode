import bisect
from typing import List

class BIT:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def add(self, idx, val):
        i = idx + 1
        while i <= self.n:
            self.bit[i] += val
            i += i & -i

    def sum(self, idx):
        i = idx + 1
        res = 0
        while i > 0:
            res += self.bit[i]
            i -= i & -i
        return res

    def find_kth(self, k):
        i = 0
        bit_mask = 1 << (self.n.bit_length() - 1)
        while bit_mask:
            t = i + bit_mask
            if t <= self.n and self.bit[t] < k:
                i = t
                k -= self.bit[t]
            bit_mask >>= 1
        return i

class Solution:
    def minAbsoluteDifference(self, nums: List[int], x: int) -> int:
        if x == 0:
            return 0
        n = len(nums)
        vals = sorted(set(nums))
        comp = {v: i for i, v in enumerate(vals)}
        bit = BIT(len(vals))
        total = 0
        ans = 10**10
        for i in range(n):
            if i >= x:
                bit.add(comp[nums[i - x]], 1)
                total += 1
            if total == 0:
                continue
            v = nums[i]
            idx = comp[v]
            freq = bit.sum(idx) - bit.sum(idx - 1)
            if freq > 0:
                return 0
            if idx > 0:
                count_less = bit.sum(idx - 1)
                if count_less > 0:
                    pred_idx = bit.find_kth(count_less)
                    ans = min(ans, abs(v - vals[pred_idx]))
            count_leq = bit.sum(idx)
            if count_leq < total:
                succ_idx = bit.find_kth(count_leq + 1)
                ans = min(ans, abs(v - vals[succ_idx]))
        return ans