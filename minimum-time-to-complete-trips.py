from typing import List

class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        min_time = min(time)
        low, high = 0, min_time * totalTrips
        while low < high:
            mid = (low + high) // 2
            trips = sum(mid // t for t in time)
            if trips >= totalTrips:
                high = mid
            else:
                low = mid + 1
        return low
