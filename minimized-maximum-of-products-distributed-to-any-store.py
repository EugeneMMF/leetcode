class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        low, high = 1, max(quantities)
        while low < high:
            mid = (low + high) // 2
            required = 0
            for q in quantities:
                required += (q + mid - 1) // mid
                if required > n:
                    break
            if required <= n:
                high = mid
            else:
                low = mid + 1
        return low
