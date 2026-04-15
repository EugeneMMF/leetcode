from typing import List

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def at_most(k):
            count = {}
            left = res = 0
            distinct = 0
            for right, val in enumerate(nums):
                if count.get(val, 0) == 0:
                    distinct += 1
                count[val] = count.get(val, 0) + 1
                while distinct > k:
                    left_val = nums[left]
                    count[left_val] -= 1
                    if count[left_val] == 0:
                        distinct -= 1
                    left += 1
                res += right - left + 1
            return res
        return at_most(k) - at_most(k - 1)
