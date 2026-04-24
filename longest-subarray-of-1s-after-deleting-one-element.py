class Solution:
    def longestSubarray(self, nums):
        left = 0
        zeros = 0
        ans = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1
            while zeros > 1:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            ans = ans if ans > right - left + 1 else right - left + 1
        return ans - 1 if ans > 0 else 0
