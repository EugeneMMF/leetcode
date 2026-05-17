from typing import List

class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        n = len(nums)
        max_or = 0
        count = 0
        for mask in range(1, 1 << n):
            cur = 0
            for i in range(n):
                if mask >> i & 1:
                    cur |= nums[i]
            if cur > max_or:
                max_or = cur
                count = 1
            elif cur == max_or:
                count += 1
        return count
