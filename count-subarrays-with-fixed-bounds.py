from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        last_min = -1
        last_max = -1
        last_invalid = -1
        count = 0
        for i, val in enumerate(nums):
            if val < minK or val > maxK:
                last_invalid = i
            if val == minK:
                last_min = i
            if val == maxK:
                last_max = i
            if last_min != -1 and last_max != -1:
                min_pos = min(last_min, last_max)
                if min_pos > last_invalid:
                    count += min_pos - last_invalid
        return count
