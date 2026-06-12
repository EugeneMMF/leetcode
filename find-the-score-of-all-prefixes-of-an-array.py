from typing import List
class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        res = []
        cur_max = 0
        prefix_sum = 0
        for x in nums:
            cur_max = x if x > cur_max else cur_max
            conv = x + cur_max
            prefix_sum += conv
            res.append(prefix_sum)
        return res