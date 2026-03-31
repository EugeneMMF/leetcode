class Solution:
    def numSubarrayBoundedMax(self, nums: list[int], left: int, right: int) -> int:
        ans = 0
        l, r = -1, -1
        for i, x in enumerate(nums):
            if x > right:
                l = i
            if x >= left:
                r = i
            ans += r - l
        return ans
