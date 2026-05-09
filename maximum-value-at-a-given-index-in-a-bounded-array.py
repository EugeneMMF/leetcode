class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        def calc(v, l):
            peak = v - 1
            if peak >= l:
                return l * (2 * peak - l + 1) // 2
            return peak * (peak + 1) // 2 + (l - peak)
        left = index
        right = n - index - 1
        low, high = 1, maxSum
        while low < high:
            mid = (low + high + 1) // 2
            total = mid + calc(mid, left) + calc(mid, right)
            if total <= maxSum:
                low = mid
            else:
                high = mid - 1
        return low
