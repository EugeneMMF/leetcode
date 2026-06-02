class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        MOD = 1000000007
        d = endPos - startPos
        if abs(d) > k or (k + d) % 2 != 0:
            return 0
        r = (k + d) // 2
        if r < 0 or r > k:
            return 0
        fact = [1] * (k + 1)
        for i in range(1, k + 1):
            fact[i] = fact[i - 1] * i % MOD
        inv_fact = [1] * (k + 1)
        inv_fact[k] = pow(fact[k], MOD - 2, MOD)
        for i in range(k, 0, -1):
            inv_fact[i - 1] = inv_fact[i] * i % MOD
        return fact[k] * inv_fact[r] % MOD * inv_fact[k - r] % MOD