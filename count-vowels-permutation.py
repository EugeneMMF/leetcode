class Solution:
    def countVowelPermutation(self, n: int) -> int:
        mod = 10**9 + 7
        a = e = i = o = u = 1
        for _ in range(2, n + 1):
            na = e % mod
            ne = (a + i) % mod
            ni = (a + e + o + u) % mod
            no = (i + u) % mod
            nu = a % mod
            a, e, i, o, u = na, ne, ni, no, nu
        return (a + e + i + o + u) % mod
