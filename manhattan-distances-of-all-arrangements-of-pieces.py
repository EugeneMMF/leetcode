class Solution:
    def distanceSum(self, m: int, n: int, k: int) -> int:
        MOD = 10**9+7
        total = m * n
        maxN = total
        fact = [1] * (maxN + 1)
        for i in range(1, maxN + 1):
            fact[i] = fact[i-1] * i % MOD
        invfact = [1] * (maxN + 1)
        invfact[maxN] = pow(fact[maxN], MOD-2, MOD)
        for i in range(maxN, 0, -1):
            invfact[i-1] = invfact[i] * i % MOD
        def comb(a, b):
            if b < 0 or b > a:
                return 0
            return fact[a] * invfact[b] % MOD * invfact[a-b] % MOD
        c = comb(total-2, k-2)
        inv6 = pow(6, MOD-2, MOD)
        sumRows = n * n % MOD * (m * (m*m - 1) % MOD) % MOD * inv6 % MOD
        sumCols = m * m % MOD * (n * (n*n - 1) % MOD) % MOD * inv6 % MOD
        sumDist = (sumRows + sumCols) % MOD
        return c * sumDist % MOD