class Solution:
    def findMaximumNumber(self, k: int, x: int) -> int:
        def count_ones(num, i):
            period = 1 << i
            half = period >> 1
            full = num // period
            res = full * half
            rem = num % period
            if rem >= half:
                res += rem - half + 1
            return res

        def accumulated(num):
            if num <= 0:
                return 0
            total = 0
            i = x
            while i <= num.bit_length():
                total += count_ones(num, i)
                i += x
            return total

        low, high = 0, 1
        while accumulated(high) <= k:
            high <<= 1
        while low < high:
            mid = (low + high + 1) // 2
            if accumulated(mid) <= k:
                low = mid
            else:
                high = mid - 1
        return low