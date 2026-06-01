from typing import List

class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        total = 0
        count = 0
        for num in nums:
            if num == 0:
                count += 1
            else:
                if count:
                    total += count * (count + 1) // 2
                    count = 0
        if count:
            total += count * (count + 1) // 2
        return total
