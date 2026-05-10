import bisect
from typing import List

class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        total = 0
        max_len = 0
        for right, val in enumerate(nums):
            total += val
            while (right - left + 1) * val - total > k:
                total -= nums[left]
                left += 1
            if right - left + 1 > max_len:
                max_len = right - left + 1
        return max_len
