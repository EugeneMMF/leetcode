class Solution:
    def maxGoodNumber(self, nums: List[int]) -> int:
        from itertools import permutations
        max_val = 0
        for perm in permutations(nums):
            bin_str = ''.join(bin(x)[2:] for x in perm)
            val = int(bin_str, 2)
            if val > max_val:
                max_val = val
        return max_val