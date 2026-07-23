class Solution:
    def countWinningSequences(self, s: str) -> int:
        mod = 1000000007
        n = len(s)
        offset = n
        # map chars to indices: F=0, W=1, E=2
        char_to_idx = {'F': 0, 'W': 1, 'E': 2}
        a_moves = [char_to_idx[c] for c in s]
        # dp[prev_move][diff_offset]
        dp_prev = [[0] * (2 * n + 1) for _ in range(3)]
        # first round
        for m in range(3):
            diff = 0
            if (m - a_moves[0] + 3) % 3 == 1:
                diff = 1
            elif (a_moves[0] - m + 3) % 3 == 1:
                diff = -1
            dp_prev[m][offset + diff] = 1
        # subsequent rounds
        for i in range(1, n):
            dp_cur = [[0] * (2 * n + 1) for _ in range(3)]
            ai = a_moves[i]
            for prev in range(3):
                row = dp_prev[prev]
                for d in range(2 * n + 1):
                    cnt = row[d]
                    if cnt == 0:
                        continue
                    for m in range(3):
                        if m == prev:
                            continue
                        diff = 0
                        if (m - ai + 3) % 3 == 1:
                            diff = 1
                        elif (ai - m + 3) % 3 == 1:
                            diff = -1
                        nd = d + diff
                        dp_cur[m][nd] = (dp_cur[m][nd] + cnt) % mod
            dp_prev = dp_cur
        # sum over positive diff
        res = 0
        for m in range(3):
            row = dp_prev[m]
            for d in range(offset + 1, 2 * n + 1):
                res = (res + row[d]) % mod
        return res