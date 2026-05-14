class Solution:
    def isThree(self, n: int) -> bool:
        import math
        r = int(math.isqrt(n))
        if r * r != n:
            return False
        if r < 2:
            return False
        for i in range(2, int(math.isqrt(r)) + 1):
            if r % i == 0:
                return False
        return True
