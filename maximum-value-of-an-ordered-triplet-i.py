from typing import List

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        suffix_max = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix_max[i] = max(nums[i], suffix_max[i + 1])
        max_val = 0
        max_left = nums[0]
        for j in range(1, n - 1):
            left_diff = max_left - nums[j]
            candidate = left_diff * suffix_max[j + 1]
            if candidate > max_val:
                max_val = candidate
            if nums[j] > max_left:
                max_left = nums[j]
        return max_val