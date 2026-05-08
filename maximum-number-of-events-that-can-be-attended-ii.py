class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        from bisect import bisect_right
        events.sort(key=lambda x: x[0])
        n = len(events)
        starts = [e[0] for e in events]
        next_idx = [0]*n
        for i in range(n):
            next_idx[i] = bisect_right(starts, events[i][1])
        dp = [[0]*(k+1) for _ in range(n+1)]
        for i in range(n-1, -1, -1):
            val = events[i][2]
            nxt = next_idx[i]
            for j in range(1, k+1):
                skip = dp[i+1][j]
                take = val + dp[nxt][j-1]
                dp[i][j] = skip if skip >= take else take
        return dp[0][k]
