import bisect
from bisect import bisect_right
from typing import List

class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]
        res = []
        for q in queries:
            idx = bisect_right(nums, q)
            left_sum = prefix[idx]
            right_sum = prefix[n] - prefix[idx]
            left_cnt = idx
            right_cnt = n - idx
            ops = q * left_cnt - left_sum + right_sum - q * right_cnt
            res.append(ops)
        return res
