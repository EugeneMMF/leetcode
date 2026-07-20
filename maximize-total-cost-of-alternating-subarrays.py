class Solution:
    def maximumTotalCost(self, nums):
        n = len(nums)
        alt_pref = [0] * (n + 1)
        for i in range(n):
            alt_pref[i + 1] = alt_pref[i] + nums[i] * (-1) ** i
        dp = [0] * (n + 1)
        best_even = 0
        best_odd = -10**30
        for i in range(1, n + 1):
            val_even = best_even + alt_pref[i]
            val_odd = best_odd - alt_pref[i]
            dp[i] = val_even if val_even > val_odd else val_odd
            if i % 2 == 0:
                cand = dp[i] - alt_pref[i]
                if cand > best_even:
                    best_even = cand
            else:
                cand = dp[i] + alt_pref[i]
                if cand > best_odd:
                    best_odd = cand
        return dp[n]