class Solution:
    def stringCount(self, n: int) -> int:
        mod = 1000000007
        pow26 = pow(26, n, mod)
        pow25 = pow(25, n, mod)
        pow24 = pow(24, n, mod)
        pow23 = pow(23, n, mod)
        pow25_n1 = pow(25, n-1, mod) if n > 0 else 1
        pow24_n1 = pow(24, n-1, mod) if n > 0 else 1
        pow23_n1 = pow(23, n-1, mod) if n > 0 else 1
        # Count of strings missing at least one required letter or having <2 e's
        L = pow25
        T = pow25
        E2 = (pow25 + n * pow25_n1) % mod
        LT = pow24
        LE2 = (pow24 + n * pow24_n1) % mod
        TE2 = LE2
        LTE2 = (pow23 + n * pow23_n1) % mod
        ans = (pow26 - (L + T + E2) + (LT + LE2 + TE2) - LTE2) % mod
        return ans
