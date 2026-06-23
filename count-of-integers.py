class Solution:
    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        mod = 10**9 + 7
        def count_le(s):
            n = len(s)
            from functools import lru_cache
            @lru_cache(None)
            def dfs(pos, sum_, tight):
                if pos == n:
                    return 1 if min_sum <= sum_ <= max_sum else 0
                limit = int(s[pos]) if tight else 9
                res = 0
                for d in range(limit + 1):
                    ntight = tight and d == limit
                    res += dfs(pos + 1, sum_ + d, ntight)
                return res % mod
            return dfs(0, 0, True)
        def dec_str(s):
            lst = list(s)
            i = len(lst) - 1
            while i >= 0 and lst[i] == '0':
                lst[i] = '9'
                i -= 1
            if i >= 0:
                lst[i] = str(int(lst[i]) - 1)
            return ''.join(lst).lstrip('0') or '0'
        total2 = count_le(num2)
        num1_minus = dec_str(num1)
        total1 = count_le(num1_minus) if num1_minus != '0' else 0
        return (total2 - total1) % mod