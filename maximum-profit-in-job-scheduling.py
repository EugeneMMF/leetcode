from typing import List
import bisect

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
        ends = [e for _, e, _ in jobs]
        n = len(jobs)
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            s, e, p = jobs[i - 1]
            idx = bisect.bisect_right(ends, s, 0, i - 1)
            dp[i] = dp[i - 1] if dp[i - 1] > dp[idx] + p else dp[idx] + p
        return dp[n]
