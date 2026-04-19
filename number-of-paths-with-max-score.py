class Solution:
    def pathsWithMaxScore(self, board):
        MOD = 10**9 + 7
        n = len(board)
        dp_max = [[-1] * n for _ in range(n)]
        dp_cnt = [[0] * n for _ in range(n)]
        si, sj = n - 1, n - 1
        dp_max[si][sj] = 0
        dp_cnt[si][sj] = 1
        for i in range(si, -1, -1):
            for j in range(sj, -1, -1):
                if board[i][j] == 'X' or (i == si and j == sj):
                    continue
                best = -1
                cnt = 0
                for ni, nj in ((i + 1, j), (i, j + 1), (i + 1, j + 1)):
                    if ni < n and nj < n and dp_max[ni][nj] != -1:
                        if dp_max[ni][nj] > best:
                            best = dp_max[ni][nj]
                            cnt = dp_cnt[ni][nj]
                        elif dp_max[ni][nj] == best:
                            cnt = (cnt + dp_cnt[ni][nj]) % MOD
                if best == -1:
                    continue
                val = 0
                if board[i][j].isdigit():
                    val = int(board[i][j])
                dp_max[i][j] = best + val
                dp_cnt[i][j] = cnt % MOD
        if dp_max[0][0] == -1:
            return [0, 0]
        return [dp_max[0][0], dp_cnt[0][0]]
