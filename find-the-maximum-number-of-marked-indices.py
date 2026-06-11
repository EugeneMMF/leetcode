class Solution:
    def maxNumOfMarkedIndices(self, nums):
        nums.sort()
        n = len(nums)
        left = 0
        right = n // 2
        count = 0
        while left < n // 2 and right < n:
            if 2 * nums[left] <= nums[right]:
                count += 2
                left += 1
                right += 1
            else:
                right += 1
        return count
