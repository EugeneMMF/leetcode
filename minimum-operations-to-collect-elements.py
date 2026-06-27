from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        target = set(range(1, k+1))
        seen = set()
        ops = 0
        for num in reversed(nums):
            ops += 1
            seen.add(num)
            if seen >= target:
                return ops
