class Solution:
    def minimumCost(self, nums):
        n = len(nums)
        min_suffix = [0] * (n + 1)
        min_suffix[n] = float('inf')
        for i in range(n - 1, -1, -1):
            min_suffix[i] = min(nums[i], min_suffix[i + 1])
        best = float('inf')
        for i in range(1, n - 1):
            best = min(best, nums[i] + min_suffix[i + 1])
        return nums[0] + best
