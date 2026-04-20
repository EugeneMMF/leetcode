from typing import List

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        freq = [0] * 101
        for v in nums:
            freq[v] += 1
        prefix = [0] * 101
        total = 0
        for i in range(101):
            prefix[i] = total
            total += freq[i]
        return [prefix[v] for v in nums]
