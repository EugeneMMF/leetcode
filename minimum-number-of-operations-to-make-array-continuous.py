from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        unique = sorted(set(nums))
        n = len(nums)
        l = 0
        maxsize = 0
        for r in range(len(unique)):
            while unique[r] - unique[l] > n - 1:
                l += 1
            size = r - l + 1
            if size > maxsize:
                maxsize = size
        return n - maxsize