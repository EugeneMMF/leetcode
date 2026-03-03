class Solution:
    def minPatches(self, nums: list[int], n: int) -> int:
        patches = 0
        reach = 0
        i = 0

        while reach < n:
            if i < len(nums) and nums[i] <= reach + 1:
                reach += nums[i]
                i += 1
            else:
                reach += (reach + 1)
                patches += 1
        
        return patches
