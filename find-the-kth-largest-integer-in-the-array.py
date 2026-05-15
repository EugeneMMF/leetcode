import typing

class Solution:
    def kthLargestNumber(self, nums: typing.List[str], k: int) -> str:
        nums.sort(key=lambda x: (len(x), x), reverse=True)
        return nums[k-1]