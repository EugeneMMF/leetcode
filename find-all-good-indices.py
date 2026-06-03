import typing
class Solution:
    def goodIndices(self, nums: typing.List[int], k: int) -> typing.List[int]:
        n = len(nums)
        left = [0] * n
        right = [0] * n
        left[0] = 1
        for i in range(1, n):
            if nums[i-1] >= nums[i]:
                left[i] = left[i-1] + 1
            else:
                left[i] = 1
        right[n-1] = 1
        for i in range(n-2, -1, -1):
            if nums[i] <= nums[i+1]:
                right[i] = right[i+1] + 1
            else:
                right[i] = 1
        res = []
        for i in range(k, n-k):
            if left[i-1] >= k and right[i+1] >= k:
                res.append(i)
        return res
