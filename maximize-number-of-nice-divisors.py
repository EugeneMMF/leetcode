class Solution:
    def maxNiceDivisors(self, primeFactors: int) -> int:
        MOD = 10**9 + 7
        if primeFactors == 1:
            return 1
        q, r = divmod(primeFactors, 3)
        if r == 0:
            return pow(3, q, MOD)
        if r == 1:
            if q == 0:
                return 1
            return (pow(3, q - 1, MOD) * 4) % MOD
        return (pow(3, q, MOD) * 2) % MOD
