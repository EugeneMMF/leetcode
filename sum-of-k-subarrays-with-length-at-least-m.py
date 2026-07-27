class Solution:
    def maxSum(self, nums: List[int], k: int, m: int) -> int:
        n = len(nums)
        pref = [0]*(n+1)
        for i in range(n):
            pref[i+1] = pref[i] + nums[i]
        neg_inf = -10**18
        dp_prev = [0]*(n+1)
        for _ in range(1, k+1):
            dp_curr = [neg_inf]*(n+1)
            best = neg_inf
            for i in range(1, n+1):
                if i-m >= 0:
                    s = i-m
                    val = dp_prev[s] - pref[s]
                    if val > best:
                        best = val
                if best != neg_inf:
                    dp_curr[i] = max(dp_curr[i-1], best + pref[i])
                else:
                    dp_curr[i] = dp_curr[i-1]
            dp_prev = dp_curr
        return dp_prev[n]
