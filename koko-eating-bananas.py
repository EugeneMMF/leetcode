from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        while low < high:
            mid = (low + high) // 2
            hours = 0
            for p in piles:
                hours += (p + mid - 1) // mid
                if hours > h:
                    break
            if hours <= h:
                high = mid
            else:
                low = mid + 1
        return low
