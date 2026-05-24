import typing

class Solution:
    def intersection(self, nums: typing.List[typing.List[int]]) -> typing.List[int]:
        result = set(nums[0])
        for arr in nums[1:]:
            result &= set(arr)
            if not result:
                return []
        return sorted(result)
