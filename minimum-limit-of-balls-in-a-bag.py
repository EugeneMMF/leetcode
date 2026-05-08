import math
from typing import List

class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        low, high = 1, max(nums)
        while low < high:
            mid = (low + high) // 2
            ops = 0
            for n in nums:
                ops += (n - 1) // mid
                if ops > maxOperations:
                    break
            if ops <= maxOperations:
                high = mid
            else:
                low = mid + 1
        return low