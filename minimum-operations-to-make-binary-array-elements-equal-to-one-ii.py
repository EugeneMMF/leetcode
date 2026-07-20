class Solution:
    def minOperations(self, nums: List[int]) -> int:
        flips = 0
        ops = 0
        for num in nums:
            if (num ^ flips) == 0:
                ops += 1
                flips ^= 1
        return ops
