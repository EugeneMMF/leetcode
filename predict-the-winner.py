class Solution:
    def predictTheWinner(self, nums: list[int]) -> bool:
        n = len(nums)

        dp = [[0] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = nums[i]

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1

                score_if_take_i = nums[i] - dp[i + 1][j]
                score_if_take_j = nums[j] - dp[i][j - 1]

                dp[i][j] = max(score_if_take_i, score_if_take_j)

        return dp[0][n - 1] >= 0
