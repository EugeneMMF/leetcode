class Solution:
    def bestTeamScore(self, scores, ages):
        players = sorted(zip(ages, scores))
        n = len(players)
        dp = [0] * n
        for i in range(n):
            dp[i] = players[i][1]
            for j in range(i):
                if players[j][1] <= players[i][1]:
                    if dp[j] + players[i][1] > dp[i]:
                        dp[i] = dp[j] + players[i][1]
        return max(dp)
