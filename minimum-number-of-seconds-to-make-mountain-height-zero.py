class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        import math
        max_t = max(workerTimes)
        high = max_t * mountainHeight * (mountainHeight + 1) // 2
        low = 0
        while low < high:
            mid = (low + high) // 2
            total = 0
            for t in workerTimes:
                limit = (2 * mid) // t
                d = 1 + 4 * limit
                sqrt_d = math.isqrt(d)
                x = (sqrt_d - 1) // 2
                total += x
                if total >= mountainHeight:
                    break
            if total >= mountainHeight:
                high = mid
            else:
                low = mid + 1
        return low
