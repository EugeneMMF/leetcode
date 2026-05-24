import typing
class Solution:
    def waysToSplitArray(self, nums: typing.List[int]) -> int:
        total = sum(nums)
        prefix = 0
        count = 0
        for i in range(len(nums)-1):
            prefix += nums[i]
            suffix = total - prefix
            if prefix >= suffix:
                count += 1
        return count
