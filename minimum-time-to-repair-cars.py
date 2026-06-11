class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        import math
        low, high = 0, max(ranks) * cars * cars
        while low < high:
            mid = (low + high) // 2
            total = 0
            for r in ranks:
                total += math.isqrt(mid // r)
                if total >= cars:
                    break
            if total >= cars:
                high = mid
            else:
                low = mid + 1
        return low