import bisect
from typing import List

class Solution:
    def minOperationsToMakeMedianK(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        m = n // 2
        ops = 0
        for i in range(m):
            if nums[i] > k:
                ops += nums[i] - k
        if nums[m] != k:
            ops += abs(nums[m] - k)
        for i in range(m + 1, n):
            if nums[i] < k:
                ops += k - nums[i]
        return ops
