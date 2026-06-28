class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        INF = 10 ** 9
        divisors = [[] for _ in range(n + 1)]
        for m in range(2, n + 1):
            for d in range(1, m):
                if m % d == 0:
                    divisors[m].append(d)
        cost = [[INF] * (n + 1) for _ in range(n + 1)]
        for l in range(n):
            for r in range(l + 2, n + 1):
                m = r - l
                best = INF
                for d in divisors[m]:
                    total = 0
                    for g in range(d):
                        t = 0
                        pos = l + g
                        while pos < r:
                            t += 1
                            pos += d
                        for i in range(t // 2):
                            a = s[l + g + i * d]
                            b = s[l + g + (t - 1 - i) * d]
                            if a != b:
                                total += 1
                    if total < best:
                        best = total
                cost[l][r] = best
        dp = [[INF] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0
        for i in range(1, n + 1):
            for j in range(1, k + 1):
                if i < j * 2:
                    continue
                for p in range((j - 1) * 2, i - 1):
                    if dp[p][j - 1] < INF and cost[p][i] < INF:
                        val = dp[p][j - 1] + cost[p][i]
                        if val < dp[i][j]:
                            dp[i][j] = val
        return dp[n][k]