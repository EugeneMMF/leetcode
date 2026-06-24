from typing import List

class Solution:
    def minCost(self, nums: List[int], x: int) -> int:
        n = len(nums)
        # pref_min[i][t] = min cost for type i with at most t operations
        pref_min = [[0] * n for _ in range(n)]
        for i in range(n):
            min_val = nums[i]
            pref_min[i][0] = min_val
            for t in range(1, n):
                idx = (i - t) % n
                if nums[idx] < min_val:
                    min_val = nums[idx]
                pref_min[i][t] = min_val
        best = 10**30
        for t in range(n):
            total = x * t
            for i in range(n):
                total += pref_min[i][t]
            if total < best:
                best = total
        return best