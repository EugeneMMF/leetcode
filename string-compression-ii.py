class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        n = len(s)
        INF = 10**9
        dp = [[INF] * (k + 1) for _ in range(n + 1)]
        for d in range(k + 1):
            dp[n][d] = 0

        def run_len(cnt: int) -> int:
            if cnt == 1:
                return 1
            if cnt < 10:
                return 2
            if cnt < 100:
                return 3
            return 4

        for i in range(n - 1, -1, -1):
            for d in range(k + 1):
                if d > 0:
                    dp[i][d] = dp[i + 1][d - 1]
                cnt = 0
                delcnt = 0
                for j in range(i, n):
                    if s[j] == s[i]:
                        cnt += 1
                    else:
                        delcnt += 1
                    if delcnt > d:
                        break
                    length = run_len(cnt)
                    dp[i][d] = min(dp[i][d], length + dp[j + 1][d - delcnt])
        return dp[0][k]
