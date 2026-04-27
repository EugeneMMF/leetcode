class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        MOD = 10**9 + 7
        max_n = n + k
        fact = [1] * (max_n + 1)
        for i in range(1, max_n + 1):
            fact[i] = fact[i - 1] * i % MOD
        inv_fact = [1] * (max_n + 1)
        inv_fact[max_n] = pow(fact[max_n], MOD - 2, MOD)
        for i in range(max_n, 0, -1):
            inv_fact[i - 1] = inv_fact[i] * i % MOD
        total = n + k - 1
        r = 2 * k
        if r > total:
            return 0
        return fact[total] * inv_fact[r] % MOD * inv_fact[total - r] % MOD
