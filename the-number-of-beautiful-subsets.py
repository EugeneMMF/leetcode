from typing import List

class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        n = len(nums)
        conflict = [0] * n
        for i in range(n):
            for j in range(n):
                if i != j and abs(nums[i] - nums[j]) == k:
                    conflict[i] |= 1 << j
        count = 0
        for mask in range(1, 1 << n):
            ok = True
            m = mask
            while m:
                lsb = m & -m
                i = lsb.bit_length() - 1
                if mask & conflict[i]:
                    ok = False
                    break
                m -= lsb
            if ok:
                count += 1
        return count
