class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        n = len(nums)
        m = len(multipliers)
        dp = [-10**18] * (m + 1)
        dp[0] = 0
        for k in range(m):
            new_dp = [-10**18] * (m + 1)
            for i in range(k + 1):
                cur = dp[i]
                if cur == -10**18:
                    continue
                # take from left
                new_dp[i + 1] = max(new_dp[i + 1], cur + multipliers[k] * nums[i])
                # take from right
                j = k - i
                new_dp[i] = max(new_dp[i], cur + multipliers[k] * nums[n - 1 - j])
            dp = new_dp
        return max(dp)
