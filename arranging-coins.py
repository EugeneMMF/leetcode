
class Solution:
    def arrangeCoins(self, n: int) -> int:
        low = 1
        high = 65536
        ans = 0
        while low <= high:
            mid = low + (high - low) // 2
            coins_needed = mid * (mid + 1) // 2
            if coins_needed <= n:
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return ans
