class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if sum(candies) < k:
            return 0
        lo, hi = 1, max(candies)
        res = 0
        while lo <= hi:
            mid = (lo + hi) // 2
            total = 0
            for c in candies:
                total += c // mid
                if total >= k:
                    break
            if total >= k:
                res = mid
                lo = mid + 1
            else:
                hi = mid - 1
        return res
