from typing import List

class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        even_sum = sum(x for x in nums if x % 2 == 0)
        res = []
        for val, idx in queries:
            old = nums[idx]
            if old % 2 == 0:
                even_sum -= old
            nums[idx] = old + val
            new = nums[idx]
            if new % 2 == 0:
                even_sum += new
            res.append(even_sum)
        return res
