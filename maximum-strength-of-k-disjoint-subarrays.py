class Solution:
    def maximumStrength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        P = [0] * (n + 1)
        for i, v in enumerate(nums, 1):
            P[i] = P[i - 1] + v
        coeff = [0] * (k + 1)
        for j in range(1, k + 1):
            coeff[j] = (k - j + 1) * (1 if j % 2 == 1 else -1)
        neg_inf = -10**30
        dp_prev = [0] * (n + 1)
        for j in range(1, k + 1):
            dp_cur = [neg_inf] * (n + 1)
            best = neg_inf
            for i in range(1, n + 1):
                best = max(best, dp_prev[i - 1] - coeff[j] * P[i - 1])
                dp_cur[i] = max(dp_cur[i - 1], best + coeff[j] * P[i])
            dp_prev = dp_cur
        return dp_prev[n]