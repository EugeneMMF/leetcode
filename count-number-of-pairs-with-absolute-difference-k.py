from typing import List

class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        freq = {}
        count = 0
        for num in nums:
            count += freq.get(num - k, 0)
            count += freq.get(num + k, 0)
            freq[num] = freq.get(num, 0) + 1
        return count
