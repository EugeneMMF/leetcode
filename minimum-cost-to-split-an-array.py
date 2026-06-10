class Solution:
    def minCost(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [10**18] * (n + 1)
        dp[0] = 0
        for j in range(n):
            cnt = {}
            unique_once = 0
            for i in range(j + 1, n + 1):
                val = nums[i - 1]
                prev = cnt.get(val, 0)
                cnt[val] = prev + 1
                if prev == 0:
                    unique_once += 1
                elif prev == 1:
                    unique_once -= 1
                # prev >1: no change
                trimmed_len = (i - j) - unique_once
                candidate = dp[j] + k + trimmed_len
                if candidate < dp[i]:
                    dp[i] = candidate
        return dp[n]