class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        n = mountainArr.length()
        lo, hi = 0, n - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if mountainArr.get(mid) < mountainArr.get(mid + 1):
                lo = mid + 1
            else:
                hi = mid
        peak = lo
        lo, hi = 0, peak
        while lo <= hi:
            mid = (lo + hi) // 2
            val = mountainArr.get(mid)
            if val == target:
                return mid
            elif val < target:
                lo = mid + 1
            else:
                hi = mid - 1
        lo, hi = peak + 1, n - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            val = mountainArr.get(mid)
            if val == target:
                return mid
            elif val > target:
                lo = mid + 1
            else:
                hi = mid - 1
        return -1
