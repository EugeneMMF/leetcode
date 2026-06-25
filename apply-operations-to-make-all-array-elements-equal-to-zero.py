from typing import List

class Solution:
    def checkArray(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        diff = [0] * (n + 1)
        current = 0
        for i in range(n):
            current += diff[i]
            remaining = nums[i] - current
            if remaining < 0:
                return False
            if remaining > 0:
                if i + k > n:
                    return False
                diff[i] += remaining
                diff[i + k] -= remaining
                current += remaining
        return True