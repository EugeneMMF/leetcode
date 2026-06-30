from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        xor = 0
        for num in nums:
            xor ^= num
        diff = xor ^ k
        return diff.bit_count()