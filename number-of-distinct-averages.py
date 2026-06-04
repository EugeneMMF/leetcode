import typing

class Solution:
    def distinctAverages(self, nums: typing.List[int]) -> int:
        nums.sort()
        s = set()
        n = len(nums)
        for i in range(n // 2):
            s.add((nums[i] + nums[n - 1 - i]) / 2)
        return len(s)
