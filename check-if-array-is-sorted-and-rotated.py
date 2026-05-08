import typing

class Solution:
    def check(self, nums: typing.List[int]) -> bool:
        n = len(nums)
        if n <= 1:
            return True
        drop = 0
        for i in range(n - 1):
            if nums[i] > nums[i + 1]:
                drop += 1
                if drop > 1:
                    return False
        if drop == 0:
            return True
        return nums[-1] <= nums[0]
