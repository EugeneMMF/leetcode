from typing import List

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        freq = {}
        for v in nums:
            freq[v] = freq.get(v, 0) + 1
        ans = 0
        for c in freq.values():
            ans += c * (c - 1) // 2
        return ans
