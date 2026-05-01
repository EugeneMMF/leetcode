class Solution:
    def waysToFillArray(self, queries):
        MOD = 10**9 + 7
        max_n = 0
        for n, _ in queries:
            if n > max_n:
                max_n = n
        limit = max_n + 100
        fact = [1] * (limit + 1)
        for i in range(1, limit + 1):
            fact[i] = fact[i - 1] * i % MOD
        inv_fact = [1] * (limit + 1)
        inv_fact[limit] = pow(fact[limit], MOD - 2, MOD)
        for i in range(limit, 0, -1):
            inv_fact[i - 1] = inv_fact[i] * i % MOD
        def comb(a, b):
            if b < 0 or b > a:
                return 0
            return fact[a] * inv_fact[b] % MOD * inv_fact[a - b] % MOD
        res = []
        for n, k in queries:
            ans = 1
            x = k
            d = 2
            while d * d <= x:
                if x % d == 0:
                    e = 0
                    while x % d == 0:
                        x //= d
                        e += 1
                    ans = ans * comb(e + n - 1, n - 1) % MOD
                d += 1 if d == 2 else 2
            if x > 1:
                ans = ans * comb(1 + n - 1, n - 1) % MOD
            res.append(ans)
        return res
