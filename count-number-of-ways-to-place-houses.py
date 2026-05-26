class Solution:
    def countHousePlacements(self, n: int) -> int:
        mod = 10**9 + 7
        a, b = 0, 1
        for _ in range(n + 2):
            a, b = b, (a + b) % mod
        fib = a
        return (fib * fib) % mod