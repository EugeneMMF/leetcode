import typing
class Solution:
    def minimumOperations(self, nums: typing.List[int]) -> int:
        return len({x for x in nums if x > 0})