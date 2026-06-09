class Solution:
    def minimizeSet(self, divisor1: int, divisor2: int, uniqueCnt1: int, uniqueCnt2: int) -> int:
        d1, d2 = divisor1, divisor2
        def lcm(a, b):
            return a // __import__('math').gcd(a, b) * b
        L = lcm(d1, d2)
        def feasible(M):
            div1 = M // d1
            div2 = M // d2
            both = M // L
            a = M - div1 - div2 + both
            b = div2 - both
            c = div1 - both
            if a < 0 or b < 0 or c < 0:
                return False
            if a + b < uniqueCnt1:
                return False
            if a + c < uniqueCnt2:
                return False
            need00 = 0
            if uniqueCnt1 > b:
                need00 += uniqueCnt1 - b
            if uniqueCnt2 > c:
                need00 += uniqueCnt2 - c
            return a >= need00
        low, high = 1, (uniqueCnt1 + uniqueCnt2) * max(d1, d2)
        while low < high:
            mid = (low + high) // 2
            if feasible(mid):
                high = mid
            else:
                low = mid + 1
        return low