class Solution:
    def nonSpecialCount(self, l: int, r: int) -> int:
        import math
        low = int(math.isqrt(l))
        if low * low < l:
            low += 1
        high = int(math.isqrt(r))
        if high < low:
            return r - l + 1
        limit = high
        sieve = bytearray(b'\x01') * (limit + 1)
        sieve[0:2] = b'\x00\x00'
        for i in range(2, int(limit ** 0.5) + 1):
            if sieve[i]:
                step = i
                start = i * i
                sieve[start:limit + 1:step] = b'\x00' * ((limit - start) // step + 1)
        count = 0
        for p in range(low, high + 1):
            if sieve[p]:
                count += 1
        return (r - l + 1) - count