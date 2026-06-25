class Solution:
    def maxScore(self, nums: List[int], x: int) -> int:
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        INF_NEG = -10**18
        best_even = dp[0] if nums[0] % 2 == 0 else INF_NEG
        best_odd = dp[0] if nums[0] % 2 == 1 else INF_NEG
        for i in range(1, n):
            val = nums[i]
            if val % 2 == 0:
                cand1 = best_even
                cand2 = best_odd - x
            else:
                cand1 = best_even - x
                cand2 = best_odd
            dp[i] = val + (cand1 if cand1 > cand2 else cand2)
            if val % 2 == 0:
                if dp[i] > best_even:
                    best_even = dp[i]
            else:
                if dp[i] > best_odd:
                    best_odd = dp[i]
        return max(dp)