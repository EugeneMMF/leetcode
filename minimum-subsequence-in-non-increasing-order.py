from typing import List

class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        total = sum(nums)
        nums.sort(reverse=True)
        cur = 0
        res = []
        for v in nums:
            cur += v
            res.append(v)
            if cur > total - cur:
                break
        return res
