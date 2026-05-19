class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            points, brain = questions[i]
            next_index = i + brain + 1
            take = points + (dp[next_index] if next_index <= n else 0)
            skip = dp[i + 1]
            dp[i] = take if take > skip else skip
        return dp[0]
