class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        arr.sort()
        n = len(arr)
        prefix = [0]
        for num in arr:
            prefix.append(prefix[-1] + num)
        import bisect
        def calc(v: int) -> int:
            idx = bisect.bisect_right(arr, v)
            return prefix[idx] + (n - idx) * v
        lo, hi = 0, arr[-1]
        while lo < hi:
            mid = (lo + hi) // 2
            if calc(mid) < target:
                lo = mid + 1
            else:
                hi = mid
        best = lo
        sum_best = calc(best)
        diff_best = abs(sum_best - target)
        if best > 0:
            sum_prev = calc(best - 1)
            diff_prev = abs(sum_prev - target)
            if diff_prev <= diff_best:
                best -= 1
        return best
