class Solution:
    def countNumbers(self, l: str, r: str, b: int) -> int:
        MOD = 10**9 + 7
        def to_base(n):
            if n == 0:
                return [0]
            digits = []
            while n:
                digits.append(n % b)
                n //= b
            return digits[::-1]
        def count_upto(x):
            if x < 0:
                return 0
            digits = to_base(x)
            n = len(digits)
            from functools import lru_cache
            @lru_cache(None)
            def dfs(pos, prev, tight, started):
                if pos == n:
                    return 1
                limit = digits[pos] if tight else b - 1
                res = 0
                for d in range(limit + 1):
                    ntight = tight and (d == limit)
                    if not started and d == 0:
                        res = (res + dfs(pos + 1, 0, ntight, False)) % MOD
                    else:
                        if not started or d >= prev:
                            res = (res + dfs(pos + 1, d, ntight, True)) % MOD
                return res
            return dfs(0, 0, True, False)
        l_int = int(l)
        r_int = int(r)
        return (count_upto(r_int) - count_upto(l_int - 1)) % MOD