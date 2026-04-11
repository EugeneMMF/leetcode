class Solution:
    def xorGame(self, nums):
        x = 0
        for n in nums:
            x ^= n
        return x == 0 or len(nums) % 2 == 0
