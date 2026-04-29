from typing import List

class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]
        total = prefix[-1]
        res = [0] * n
        for i in range(n):
            left = nums[i] * i - prefix[i]
            right = (total - prefix[i + 1]) - nums[i] * (n - i - 1)
            res[i] = left + right
        return res
