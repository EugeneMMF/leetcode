class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        from collections import Counter
        freq = Counter(power)
        items = sorted((v, v * cnt) for v, cnt in freq.items())
        n = len(items)
        values = [v for v, w in items]
        weights = [w for v, w in items]
        dp = [0] * n
        j = -1
        for i in range(n):
            while j + 1 < n and values[j + 1] <= values[i] - 3:
                j += 1
            take = weights[i] + (dp[j] if j >= 0 else 0)
            skip = dp[i - 1] if i > 0 else 0
            dp[i] = take if take > skip else skip
        return dp[-1] if n > 0 else 0
