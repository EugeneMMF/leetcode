class Solution:
    def numberOfBeautifulIntegers(self, low: int, high: int, k: int) -> int:
        def count(n: int) -> int:
            if n < 0:
                return 0
            digits = list(map(int, str(n)))
            L = len(digits)
            from functools import lru_cache
            @lru_cache(None)
            def dfs(pos: int, tight: int, started: int, diff: int, mod: int) -> int:
                if pos == L:
                    return 1 if started and diff == 0 and mod == 0 else 0
                limit = digits[pos] if tight else 9
                total = 0
                for d in range(0, limit + 1):
                    ntight = tight and d == limit
                    nstarted = started or d != 0
                    ndiff = diff
                    nmod = mod
                    if nstarted:
                        ndiff += 1 if d % 2 == 0 else -1
                        nmod = (mod * 10 + d) % k
                    total += dfs(pos + 1, ntight, nstarted, ndiff, nmod)
                return total
            return dfs(0, 1, 0, 0, 0)
        return count(high) - count(low - 1)