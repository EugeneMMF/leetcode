class Solution:
    def minSpaceWastedKResizing(self, nums: List[int], k: int) -> int:
        n = len(nums)
        max_segments = k + 1
        INF = 10**18
        dp = [[INF] * (max_segments + 1) for _ in range(n + 1)]
        dp[0][0] = 0
        for i in range(1, n + 1):
            for m in range(1, min(i, max_segments) + 1):
                max_val = 0
                sum_val = 0
                for j in range(i - 1, m - 2, -1):
                    max_val = max(max_val, nums[j])
                    sum_val += nums[j]
                    waste = (i - j) * max_val - sum_val
                    if dp[j][m - 1] + waste < dp[i][m]:
                        dp[i][m] = dp[j][m - 1] + waste
        return min(dp[n][1:max_segments + 1])