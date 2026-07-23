class Solution:
    def numberOfWays(self, n: int, x: int, y: int) -> int:
        MOD = 10**9 + 7
        max_val = max(n, x)
        fact = [1] * (max_val + 1)
        for i in range(1, max_val + 1):
            fact[i] = fact[i-1] * i % MOD
        invfact = [1] * (max_val + 1)
        invfact[max_val] = pow(fact[max_val], MOD-2, MOD)
        for i in range(max_val, 0, -1):
            invfact[i-1] = invfact[i] * i % MOD
        S = [[0]*(n+1) for _ in range(n+1)]
        S[0][0] = 1
        for i in range(1, n+1):
            for k in range(1, i+1):
                S[i][k] = (k * S[i-1][k] + S[i-1][k-1]) % MOD
        res = 0
        max_k = min(n, x)
        for k in range(1, max_k+1):
            comb = fact[x] * invfact[k] % MOD * invfact[x-k] % MOD
            ways = comb * fact[k] % MOD * S[n][k] % MOD * pow(y, k, MOD) % MOD
            res = (res + ways) % MOD
        return res
