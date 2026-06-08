class Solution:
    def pivotInteger(self, n: int) -> int:
        import math
        val = n * (n + 1) // 2
        x = math.isqrt(val)
        if x * x == val:
            return x
        return -1
