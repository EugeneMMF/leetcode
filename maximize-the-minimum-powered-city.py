class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        n = len(stations)
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + stations[i]
        coverage = [0] * n
        for j in range(n):
            l = max(0, j - r)
            rpos = min(n, j + r + 1)
            coverage[j] = pref[rpos] - pref[l]
        min_cov = min(coverage)
        low, high = min_cov, min_cov + k
        def can(x):
            diff = [0] * (n + 1)
            added = 0
            used = 0
            for j in range(n):
                added += diff[j]
                cur = coverage[j] + added
                if cur < x:
                    need = x - cur
                    used += need
                    if used > k:
                        return False
                    added += need
                    i = j + r
                    if i >= n:
                        i = n - 1
                    end = i + r + 1
                    if end < len(diff):
                        diff[end] -= need
            return True
        while low < high:
            mid = (low + high + 1) // 2
            if can(mid):
                low = mid
            else:
                high = mid - 1
        return low