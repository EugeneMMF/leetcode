from typing import List

class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        max_sum = 0
        n = len(nums)
        for i in range(n // 2):
            s = nums[i] + nums[n - 1 - i]
            if s > max_sum:
                max_sum = s
        return max_sum
