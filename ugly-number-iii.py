import math

class Solution:
    def nthUglyNumber(self, n, a, b, c):
        def lcm(x, y):
            return x // math.gcd(x, y) * y
        ab = lcm(a, b)
        ac = lcm(a, c)
        bc = lcm(b, c)
        abc = lcm(ab, c)
        def count(x):
            return x // a + x // b + x // c - x // ab - x // ac - x // bc + x // abc
        lo, hi = 1, 2000000000
        while lo < hi:
            mid = (lo + hi) // 2
            if count(mid) >= n:
                hi = mid
            else:
                lo = mid + 1
        return lo
