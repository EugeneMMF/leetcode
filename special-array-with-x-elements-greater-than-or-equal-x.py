from typing import List

class Solution:
    def specialArray(self, nums: List[int]) -> int:
        n = len(nums)
        for x in range(n + 1):
            cnt = sum(1 for v in nums if v >= x)
            if cnt == x:
                return x
        return -1
