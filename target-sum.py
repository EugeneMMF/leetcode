class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        total_sum = sum(nums)

        if (target + total_sum) % 2 != 0 or target + total_sum < 0:
            return 0
        
        subset_sum_target = (target + total_sum) // 2

        dp = [0] * (subset_sum_target + 1)
        dp[0] = 1

        for num in nums:
            for s in range(subset_sum_target, num - 1, -1):
                dp[s] += dp[s - num]

        return dp[subset_sum_target]
