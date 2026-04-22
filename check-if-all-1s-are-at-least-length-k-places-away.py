from typing import List

class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        last = -k - 1
        for i, v in enumerate(nums):
            if v:
                if i - last - 1 < k:
                    return False
                last = i
        return True
