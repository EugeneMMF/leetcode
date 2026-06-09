class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        price.sort()
        def can(d):
            count = 1
            last = price[0]
            for p in price[1:]:
                if p - last >= d:
                    count += 1
                    last = p
                    if count == k:
                        return True
            return False
        low, high = 0, price[-1] - price[0]
        while low < high:
            mid = (low + high + 1) // 2
            if can(mid):
                low = mid
            else:
                high = mid - 1
        return low