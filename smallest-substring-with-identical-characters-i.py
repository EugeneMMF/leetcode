class Solution:
    def minLength(self, s: str, numOps: int) -> int:
        n = len(s)
        INF = 10**9

        def feasible(L: int) -> bool:
            dp = [[INF] * (L + 1) for _ in range(2)]
            bit0 = 0
            bit1 = 1
            if s[0] == '0':
                dp[0][1] = 0
            else:
                dp[0][1] = 1
            if s[0] == '1':
                dp[1][1] = 0
            else:
                dp[1][1] = 1
            for i in range(1, n):
                ndp = [[INF] * (L + 1) for _ in range(2)]
                for prev_bit in (0, 1):
                    for prev_len in range(1, L + 1):
                        cur_flips = dp[prev_bit][prev_len]
                        if cur_flips == INF:
                            continue
                        for cur_bit in (0, 1):
                            add = 0 if (s[i] == ('1' if cur_bit else '0')) else 1
                            if cur_bit == prev_bit:
                                new_len = prev_len + 1
                            else:
                                new_len = 1
                            if new_len > L:
                                continue
                            if cur_flips + add < ndp[cur_bit][new_len]:
                                ndp[cur_bit][new_len] = cur_flips + add
                dp = ndp
            min_flips = min(min(row) for row in dp)
            return min_flips <= numOps

        low, high = 1, n
        while low < high:
            mid = (low + high) // 2
            if feasible(mid):
                high = mid
            else:
                low = mid + 1
        return low