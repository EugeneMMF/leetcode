class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        L = len(s)
        pow10 = 10 ** L
        base = int(s)
        low = (start - base + pow10 - 1) // pow10 if start - base > 0 else 0
        high = (finish - base) // pow10
        if high < 0:
            return 0
        from functools import lru_cache
        def count_leq(N: int) -> int:
            if N < 0:
                return 0
            digits = list(map(int, str(N)))
            n = len(digits)
            @lru_cache(None)
            def dfs(pos: int, tight: bool, started: bool) -> int:
                if pos == n:
                    return 1
                res = 0
                max_digit = digits[pos] if tight else 9
                for d in range(0, max_digit + 1):
                    if d > limit:
                        continue
                    ntight = tight and d == max_digit
                    nstarted = started or d != 0
                    res += dfs(pos + 1, ntight, nstarted)
                return res
            return dfs(0, True, False)
        return count_leq(high) - count_leq(low - 1)
