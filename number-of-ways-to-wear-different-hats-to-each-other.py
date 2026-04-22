class Solution:
    def numberWays(self, hats):
        MOD = 10**9 + 7
        n = len(hats)
        full = (1 << n) - 1
        hat_to_people = [[] for _ in range(41)]
        for i, lst in enumerate(hats):
            for h in lst:
                hat_to_people[h].append(i)
        dp = [0] * (1 << n)
        dp[0] = 1
        for h in range(1, 41):
            for mask in range(full, -1, -1):
                if dp[mask] == 0:
                    continue
                for p in hat_to_people[h]:
                    if not (mask >> p) & 1:
                        new_mask = mask | (1 << p)
                        dp[new_mask] = (dp[new_mask] + dp[mask]) % MOD
        return dp[full]
