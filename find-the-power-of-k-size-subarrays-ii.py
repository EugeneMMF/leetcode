
from typing import List

class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if k == 1:
            return nums.copy()
        inc = [1 if nums[i+1] == nums[i] + 1 else 0 for i in range(n-1)]
        window_sum = sum(inc[:k-1])
        res = []
        for i in range(n - k + 1):
            if window_sum == k - 1:
                res.append(nums[i + k - 1])
            else:
                res.append(-1)
            if i + k - 1 < len(inc):
                window_sum += inc[i + k - 1]
            window_sum -= inc[i]
        return res
