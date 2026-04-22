from collections import deque
from typing import List

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        min_d = deque()
        max_d = deque()
        left = 0
        res = 0
        for right, val in enumerate(nums):
            while min_d and val < min_d[-1]:
                min_d.pop()
            min_d.append(val)
            while max_d and val > max_d[-1]:
                max_d.pop()
            max_d.append(val)
            while max_d[0] - min_d[0] > limit:
                if nums[left] == min_d[0]:
                    min_d.popleft()
                if nums[left] == max_d[0]:
                    max_d.popleft()
                left += 1
            res = max(res, right - left + 1)
        return res
