class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        import math
        MOD = 10**9 + 7
        lcm = a // math.gcd(a, b) * b
        low, high = 1, n * min(a, b)
        while low < high:
            mid = (low + high) // 2
            cnt = mid // a + mid // b - mid // lcm
            if cnt < n:
                low = mid + 1
            else:
                high = mid
        return low % MOD
