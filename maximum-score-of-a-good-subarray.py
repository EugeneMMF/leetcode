from typing import List

class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left = k
        right = k
        min_val = nums[k]
        best = min_val
        while left > 0 or right < n - 1:
            if left == 0:
                right += 1
                min_val = min(min_val, nums[right])
            elif right == n - 1:
                left -= 1
                min_val = min(min_val, nums[left])
            else:
                if nums[left - 1] > nums[right + 1]:
                    left -= 1
                    min_val = min(min_val, nums[left])
                else:
                    right += 1
                    min_val = min(min_val, nums[right])
            best = max(best, min_val * (right - left + 1))
        return best
