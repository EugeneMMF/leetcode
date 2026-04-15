class Solution:
    def largestSumAfterKNegations(self, nums, k):
        nums.sort()
        i = 0
        n = len(nums)
        while i < n and k > 0 and nums[i] < 0:
            nums[i] = -nums[i]
            k -= 1
            i += 1
        total = sum(nums)
        if k % 2 == 1:
            total -= 2 * min(nums)
        return total
