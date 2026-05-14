class Solution:
    def minimumPerimeter(self, neededApples: int) -> int:
        lo, hi = 1, 2000000
        while lo < hi:
            mid = (lo + hi) // 2
            apples = 2 * (2 * mid + 1) * mid * (mid + 1)
            if apples >= neededApples:
                hi = mid
            else:
                lo = mid + 1
        return 8 * lo