class Solution:
    def countSteppingNumbers(self, low: str, high: str) -> int:
        mod = 1000000007
        def count_leq(n: str) -> int:
            from functools import lru_cache
            digits = list(map(int, n))
            L = len(digits)
            @lru_cache(maxsize=None)
            def dfs(pos: int, tight: bool, last: int, started: bool) -> int:
                if pos == L:
                    return 1 if started else 0
                limit = digits[pos] if tight else 9
                res = 0
                for d in range(0, limit + 1):
                    ntight = tight and (d == limit)
                    if not started:
                        if d == 0:
                            res += dfs(pos + 1, ntight, last, False)
                        else:
                            res += dfs(pos + 1, ntight, d, True)
                    else:
                        if abs(d - last) == 1:
                            res += dfs(pos + 1, ntight, d, True)
                    if res >= mod:
                        res -= mod
                return res
            return dfs(0, True, -1, False)
        def dec_str(s: str) -> str:
            if s == "0":
                return "0"
            lst = list(s)
            i = len(lst) - 1
            while i >= 0:
                if lst[i] == '0':
                    lst[i] = '9'
                    i -= 1
                else:
                    lst[i] = chr(ord(lst[i]) - 1)
                    break
            if lst[0] == '0':
                lst = lst[1:]
            return ''.join(lst) if lst else "0"
        high_cnt = count_leq(high)
        low_minus_one = dec_str(low)
        low_cnt = count_leq(low_minus_one)
        return (high_cnt - low_cnt) % mod
