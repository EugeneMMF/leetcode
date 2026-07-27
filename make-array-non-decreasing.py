class Solution:
    def maximumPossibleSize(self, nums):
        cur_max = nums[0]
        count = 1
        for x in nums[1:]:
            if x >= cur_max:
                count += 1
                cur_max = x
        return count