import math
from typing import List

class Solution:
    def minimumFinishTime(self, tires: List[List[int]], changeTime: int, numLaps: int) -> int:
        # Filter dominated tires
        tires.sort(key=lambda x: (x[0], x[1]))
        filtered = []
        min_r = math.inf
        for f, r in tires:
            if r < min_r:
                filtered.append((f, r))
                min_r = r
        # Precompute best time for k consecutive laps
        INF = 10**18
        best_k = [INF] * (numLaps + 1)
        for f, r in filtered:
            time = 0
            mult = 1
            for k in range(1, numLaps + 1):
                time += f * mult
                if time < best_k[k]:
                    best_k[k] = time
                mult *= r
        # DP
        dp = [INF] * (numLaps + 1)
        dp[0] = 0
        for l in range(1, numLaps + 1):
            # start with a segment of l laps
            dp[l] = min(dp[l], best_k[l])
            # split into previous segment and a new one
            for k in range(1, l):
                val = dp[l - k] + changeTime + best_k[k]
                if val < dp[l]:
                    dp[l] = val
        return dp[numLaps]
