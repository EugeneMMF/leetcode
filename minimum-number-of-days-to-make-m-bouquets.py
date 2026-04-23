class Solution:
    def minDays(self, bloomDay, m, k):
        if m * k > len(bloomDay):
            return -1
        lo, hi = min(bloomDay), max(bloomDay)
        def canMake(days):
            bouquets = 0
            cnt = 0
            for d in bloomDay:
                if d <= days:
                    cnt += 1
                    if cnt == k:
                        bouquets += 1
                        cnt = 0
                        if bouquets >= m:
                            return True
                else:
                    cnt = 0
            return bouquets >= m
        while lo < hi:
            mid = (lo + hi) // 2
            if canMake(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
