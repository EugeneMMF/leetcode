from typing import List

class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]
        total = 0
        for i in range(n):
            start = i - nums[i]
            if start < 0:
                start = 0
            total += prefix[i + 1] - prefix[start]
        return total
