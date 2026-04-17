class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        MOD = 1000000007
        is_prime = [True] * (n + 1)
        if n >= 0:
            is_prime[0] = False
        if n >= 1:
            is_prime[1] = False
        p = 2
        while p * p <= n:
            if is_prime[p]:
                for i in range(p * p, n + 1, p):
                    is_prime[i] = False
            p += 1
        prime_cnt = sum(is_prime)
        fact_prime = 1
        for i in range(2, prime_cnt + 1):
            fact_prime = fact_prime * i % MOD
        fact_non = 1
        for i in range(2, n - prime_cnt + 1):
            fact_non = fact_non * i % MOD
        return fact_prime * fact_non % MOD
