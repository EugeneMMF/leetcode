class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        n = len(nums)
        max_len = 0
        for l in range(n):
            if nums[l] % 2 != 0 or nums[l] > threshold:
                continue
            length = 1
            prev_parity = nums[l] % 2
            r = l + 1
            while r < n and nums[r] <= threshold and nums[r] % 2 != prev_parity:
                length += 1
                prev_parity = nums[r] % 2
                r += 1
            if length > max_len:
                max_len = length
        return max_len
