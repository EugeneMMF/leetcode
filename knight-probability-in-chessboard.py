class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        if k == 0:
            return 1.0

        dr = [-2, -2, -1, -1, 1, 1, 2, 2]
        dc = [-1, 1, -2, 2, -2, 2, -1, 1]

        dp_prev = [[0.0] * n for _ in range(n)]
        dp_curr = [[0.0] * n for _ in range(n)]

        dp_prev[row][column] = 1.0

        for step in range(1, k + 1):
            for r_idx in range(n):
                for c_idx in range(n):
                    dp_curr[r_idx][c_idx] = 0.0

            for r in range(n):
                for c in range(n):
                    if dp_prev[r][c] > 0:
                        for i in range(8):
                            next_r = r + dr[i]
                            next_c = c + dc[i]

                            if 0 <= next_r < n and 0 <= next_c < n:
                                dp_curr[next_r][next_c] += dp_prev[r][c] / 8.0
            
            dp_prev, dp_curr = dp_curr, dp_prev

        total_probability = 0.0
        for r in range(n):
            for c in range(n):
                total_probability += dp_prev[r][c]
        
        return total_probability
