class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        import math
        g = math.gcd(a, b)
        cnt = 0
        i = 1
        while i * i <= g:
            if g % i == 0:
                cnt += 1
                if i * i != g:
                    cnt += 1
            i += 1
        return cnt
