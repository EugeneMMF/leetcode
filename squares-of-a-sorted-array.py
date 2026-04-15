from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        left, right = 0, n - 1
        pos = n - 1
        while left <= right:
            l_sq = nums[left] * nums[left]
            r_sq = nums[right] * nums[right]
            if l_sq > r_sq:
                res[pos] = l_sq
                left += 1
            else:
                res[pos] = r_sq
                right -= 1
            pos -= 1
        return res
