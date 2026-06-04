from typing import List

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if k > n:
            return 0
        freq = {}
        distinct = 0
        current_sum = 0
        max_sum = 0
        left = 0
        for right, val in enumerate(nums):
            current_sum += val
            freq[val] = freq.get(val, 0) + 1
            if freq[val] == 1:
                distinct += 1
            else:
                # duplicate added
                pass
            while right - left + 1 > k:
                rem = nums[left]
                current_sum -= rem
                freq[rem] -= 1
                if freq[rem] == 0:
                    distinct -= 1
                left += 1
            if right - left + 1 == k and distinct == k:
                if current_sum > max_sum:
                    max_sum = current_sum
        return max_sum
