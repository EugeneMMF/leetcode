class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        mod = 1000000007
        b = n - k
        if b <= 0 or b > n:
            return 0
        fact = [1] * (n + 1)
        for i in range(1, n + 1):
            fact[i] = fact[i - 1] * i % mod
        inv_fact = [1] * (n + 1)
        inv_fact[n] = pow(fact[n], mod - 2, mod)
        for i in range(n, 0, -1):
            inv_fact[i - 1] = inv_fact[i] * i % mod
        comb = fact[n - 1] * inv_fact[b - 1] % mod * inv_fact[n - b] % mod
        val_assign = m * pow(m - 1, b - 1, mod) % mod
        return comb * val_assign % mod
