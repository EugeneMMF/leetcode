class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        total = 0
        for idx, val in enumerate(nums):
            if idx.bit_count() == k:
                total += val
        return total