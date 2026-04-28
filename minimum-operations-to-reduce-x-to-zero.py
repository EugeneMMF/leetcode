from typing import List

class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        total = sum(nums)
        target = total - x
        if target < 0:
            return -1
        if target == 0:
            return len(nums)
        n = len(nums)
        left = 0
        cur = 0
        max_len = -1
        for right in range(n):
            cur += nums[right]
            while cur > target and left <= right:
                cur -= nums[left]
                left += 1
            if cur == target:
                max_len = max(max_len, right - left + 1)
        return -1 if max_len == -1 else n - max_len
