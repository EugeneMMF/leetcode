import math
from typing import List

class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        n = right
        sieve = bytearray(b'\x01') * (n + 1)
        sieve[:2] = b'\x00\x00'
        for i in range(2, int(math.isqrt(n)) + 1):
            if sieve[i]:
                step = i
                start = i * i
                sieve[start:n + 1:step] = b'\x00' * (((n - start) // step) + 1)
        primes = [i for i in range(left, right + 1) if sieve[i]]
        if len(primes) < 2:
            return [-1, -1]
        min_diff = float('inf')
        ans = [-1, -1]
        for i in range(1, len(primes)):
            d = primes[i] - primes[i - 1]
            if d < min_diff:
                min_diff = d
                ans = [primes[i - 1], primes[i]]
        return ans
