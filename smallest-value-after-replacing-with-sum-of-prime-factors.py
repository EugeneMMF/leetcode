class Solution:
    def smallestValue(self, n: int) -> int:
        def is_prime(x: int) -> bool:
            if x <= 1:
                return False
            if x <= 3:
                return True
            if x % 2 == 0 or x % 3 == 0:
                return False
            i = 5
            while i * i <= x:
                if x % i == 0 or x % (i + 2) == 0:
                    return False
                i += 6
            return True
        def sum_prime_factors(x: int) -> int:
            s = 0
            d = 2
            while d * d <= x:
                while x % d == 0:
                    s += d
                    x //= d
                d += 1
            if x > 1:
                s += x
            return s
        while True:
            if is_prime(n):
                return n
            s = sum_prime_factors(n)
            if s == n:
                return n
            n = s