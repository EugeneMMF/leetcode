
class Solution:
    def largestDivisibleSubset(self, nums: list[int]) -> list[int]:
        if not nums:
            return []

        nums.sort()

        n = len(nums)
        dp = [[num] for num in nums]

        max_subset_found = dp[0]

        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if len(dp[j]) + 1 > len(dp[i]):
                        dp[i] = dp[j] + [nums[i]]
            
            if len(dp[i]) > len(max_subset_found):
                max_subset_found = dp[i]
        
        return max_subset_found
