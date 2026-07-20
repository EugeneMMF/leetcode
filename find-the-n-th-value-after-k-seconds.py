class Solution:
    def valueAfterKSeconds(self, n: int, k: int) -> int:
        mod = 10**9 + 7
        size = n + k
        fact = [1] * (size + 1)
        for i in range(1, size + 1):
            fact[i] = fact[i - 1] * i % mod
        invfact = [1] * (size + 1)
        invfact[size] = pow(fact[size], mod - 2, mod)
        for i in range(size, 0, -1):
            invfact[i - 1] = invfact[i] * i % mod
        ans = fact[n + k - 1] * invfact[n - 1] % mod * invfact[k] % mod
        return ans
