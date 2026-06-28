class Solution:
    def minIncrementOperations(self, nums, k):
        INF = 10**18
        dp0 = 0
        dp1 = INF
        dp2 = INF
        for a in nums:
            if a >= k:
                new_dp0 = min(dp0, dp1, dp2)
                new_dp1 = INF
                new_dp2 = INF
            else:
                cost = k - a
                new_dp0 = min(dp0, dp1, dp2) + cost
                new_dp1 = dp0
                new_dp2 = dp1
            dp0, dp1, dp2 = new_dp0, new_dp1, new_dp2
        return min(dp0, dp1, dp2)
