class Solution:
    def maxRemovals(self, source: str, pattern: str, targetIndices: List[int]) -> int:
        n, m = len(source), len(pattern)
        target_set = set(targetIndices)
        INF = 10**9
        dp = [INF] * (m + 1)
        dp[0] = 0
        for i, ch in enumerate(source):
            # iterate j from m down to 1
            for j in range(m, 0, -1):
                if ch == pattern[j - 1] and dp[j - 1] != INF:
                    cost = dp[j - 1] + (1 if i in target_set else 0)
                    if cost < dp[j]:
                        dp[j] = cost
        kept = dp[m]
        return len(targetIndices) - kept
