from typing import List

class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        n = len(nums)
        total = sum(nums)
        prefix = 0
        best_idx = 0
        best_diff = float('inf')
        for i, val in enumerate(nums):
            prefix += val
            left_avg = prefix // (i + 1)
            right_len = n - i - 1
            right_avg = (total - prefix) // right_len if right_len else 0
            diff = abs(left_avg - right_avg)
            if diff < best_diff:
                best_diff = diff
                best_idx = i
        return best_idx