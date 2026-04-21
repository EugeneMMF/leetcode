class Solution:
    def numOfWays(self, n: int) -> int:
        MOD = 10**9 + 7
        a, b = 6, 6
        for _ in range(1, n):
            a, b = (a * 3 + b * 2) % MOD, (a * 2 + b * 2) % MOD
        return (a + b) % MOD
