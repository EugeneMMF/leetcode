from typing import List

class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        for i in range(n - 2 * k + 1):
            inc1 = True
            for j in range(i, i + k - 1):
                if nums[j] >= nums[j + 1]:
                    inc1 = False
                    break
            if not inc1:
                continue
            inc2 = True
            for j in range(i + k, i + 2 * k - 1):
                if nums[j] >= nums[j + 1]:
                    inc2 = False
                    break
            if inc2:
                return True
        return False
