class Solution:
    def avoidFlood(self, rains):
        from bisect import bisect_right
        n = len(rains)
        ans = [-1] * n
        zero_days = []
        last = {}
        for i, r in enumerate(rains):
            if r > 0:
                if r in last:
                    prev = last[r]
                    pos = bisect_right(zero_days, prev)
                    if pos == len(zero_days) or zero_days[pos] >= i:
                        return []
                    dry_day = zero_days.pop(pos)
                    ans[dry_day] = r
                last[r] = i
            else:
                zero_days.append(i)
                ans[i] = 1
        return ans
