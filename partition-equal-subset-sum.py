class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        total_sum = sum(nums)

        # If the total sum is odd, it's impossible to partition into two equal subsets
        if total_sum % 2 != 0:
            return False

        target = total_sum // 2

        # dp[i] will be true if a sum 'i' can be achieved using elements from nums
        dp = [False] * (target + 1)
        dp[0] = True  # A sum of 0 can always be achieved (by choosing no elements)

        for num in nums:
            # Iterate backwards from target down to num.
            # This ensures that each number 'num' is considered only once for forming a sum 'j'.
            # If we iterate forwards, 'num' could be used multiple times within the same outer loop iteration.
            for j in range(target, num - 1, -1):
                dp[j] = dp[j] or dp[j - num]

        # After processing all numbers, dp[target] will tell us if the target sum is achievable
        return dp[target]
