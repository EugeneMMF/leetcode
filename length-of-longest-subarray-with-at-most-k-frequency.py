class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        freq = {}
        left = 0
        max_len = 0
        for right, val in enumerate(nums):
            freq[val] = freq.get(val, 0) + 1
            while freq[val] > k:
                freq[nums[left]] -= 1
                left += 1
            current_len = right - left + 1
            if current_len > max_len:
                max_len = current_len
        return max_len