class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0
        candidates = {nums[0] + nums[1], nums[-1] + nums[-2], nums[0] + nums[-1]}
        best_ops = 0
        for target in candidates:
            dp = [[0] * n for _ in range(n)]
            for length in range(2, n + 1):
                for l in range(0, n - length + 1):
                    r = l + length - 1
                    best = 0
                    if l + 1 <= r and nums[l] + nums[l + 1] == target:
                        val = 1 + (dp[l + 2][r] if l + 2 <= r else 0)
                        if val > best:
                            best = val
                    if l <= r - 1 and nums[r - 1] + nums[r] == target:
                        val = 1 + (dp[l][r - 2] if l <= r - 2 else 0)
                        if val > best:
                            best = val
                    if l < r and nums[l] + nums[r] == target:
                        val = 1 + (dp[l + 1][r - 1] if l + 1 <= r - 1 else 0)
                        if val > best:
                            best = val
                    dp[l][r] = best
            if dp[0][n - 1] > best_ops:
                best_ops = dp[0][n - 1]
        return best_ops