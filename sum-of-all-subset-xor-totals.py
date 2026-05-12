class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n = len(nums)
        total = 0
        power = 1 << (n - 1)
        for bit in range(31):
            count = sum((num >> bit) & 1 for num in nums)
            if count:
                total += (1 << bit) * power
        return total