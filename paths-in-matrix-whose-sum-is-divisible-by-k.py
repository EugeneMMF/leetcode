class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        MOD = 10**9+7
        m, n = len(grid), len(grid[0])
        prev_row = [[0]*k for _ in range(n)]
        for i in range(m):
            curr_row = [[0]*k for _ in range(n)]
            for j in range(n):
                val = grid[i][j] % k
                if i == 0 and j == 0:
                    curr_row[j][val] = 1
                    continue
                count_top = prev_row[j] if i > 0 else None
                count_left = curr_row[j-1] if j > 0 else None
                for r in range(k):
                    cnt = 0
                    if count_top is not None:
                        cnt += count_top[r]
                    if count_left is not None:
                        cnt += count_left[r]
                    if cnt:
                        new_r = (r + val) % k
                        curr_row[j][new_r] = (curr_row[j][new_r] + cnt) % MOD
            prev_row = curr_row
        return prev_row[n-1][0]