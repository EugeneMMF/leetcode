class Solution:
    def minDifficulty(self, jobDifficulty, d):
        n = len(jobDifficulty)
        if n < d:
            return -1
        INF = 10**9
        dpPrev = [INF] * n
        maxJob = 0
        for i in range(n):
            maxJob = max(maxJob, jobDifficulty[i])
            dpPrev[i] = maxJob
        for day in range(2, d + 1):
            dpCurr = [INF] * n
            for i in range(day - 1, n):
                maxJob = 0
                for j in range(i, day - 2, -1):
                    maxJob = max(maxJob, jobDifficulty[j])
                    if dpPrev[j - 1] + maxJob < dpCurr[i]:
                        dpCurr[i] = dpPrev[j - 1] + maxJob
            dpPrev = dpCurr
        return dpPrev[-1] if dpPrev[-1] < INF else -1
