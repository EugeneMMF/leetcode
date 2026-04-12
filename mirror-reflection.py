class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        from math import gcd
        l = p * q // gcd(p, q)
        m = l // p
        n = l // q
        east = m % 2 == 1
        north = n % 2 == 1
        if east and north:
            return 1
        if not east and north:
            return 0
        return 2
