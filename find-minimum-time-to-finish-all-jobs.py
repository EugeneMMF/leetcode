from typing import List

class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        jobs.sort(reverse=True)
        low, high = max(jobs), sum(jobs)
        def can(limit):
            loads = [0] * k
            def dfs(idx):
                if idx == len(jobs):
                    return True
                seen = set()
                for i in range(k):
                    if loads[i] + jobs[idx] <= limit and loads[i] not in seen:
                        seen.add(loads[i])
                        loads[i] += jobs[idx]
                        if dfs(idx + 1):
                            return True
                        loads[i] -= jobs[idx]
                    if loads[i] == 0:
                        break
                return False
            return dfs(0)
        while low < high:
            mid = (low + high) // 2
            if can(mid):
                high = mid
            else:
                low = mid + 1
        return low
