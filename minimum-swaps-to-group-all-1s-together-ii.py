from typing import List

class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        k = sum(nums)
        if k == 0 or k == n:
            return 0
        zeros = sum(1 for i in range(k) if nums[i] == 0)
        min_zeros = zeros
        for i in range(1, n):
            out = nums[i-1]
            inn = nums[(i + k - 1) % n]
            if out == 0:
                zeros -= 1
            if inn == 0:
                zeros += 1
            if zeros < min_zeros:
                min_zeros = zeros
        return min_zeros
