class Solution:
    def minTaps(self, n: int, ranges):
        maxReach = [0] * (n + 1)
        for i, r in enumerate(ranges):
            left = max(0, i - r)
            right = min(n, i + r)
            if maxReach[left] < right:
                maxReach[left] = right
        taps = 0
        cur_end = 0
        next_end = 0
        i = 0
        while i <= n:
            while i <= n and i <= cur_end:
                if maxReach[i] > next_end:
                    next_end = maxReach[i]
                i += 1
            if cur_end == n:
                break
            if next_end == cur_end:
                return -1
            taps += 1
            cur_end = next_end
        return taps if cur_end >= n else -1
