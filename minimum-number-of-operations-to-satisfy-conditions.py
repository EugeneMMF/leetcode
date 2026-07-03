class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        freq = [[0]*10 for _ in range(n)]
        for i in range(m):
            row = grid[i]
            for j in range(n):
                freq[j][row[j]] += 1
        prev = freq[0][:]
        for j in range(1, n):
            best_val = -1
            best_idx = -1
            second_best = -1
            for v in range(10):
                val = prev[v]
                if val > best_val:
                    second_best = best_val
                    best_val = val
                    best_idx = v
                elif val > second_best:
                    second_best = val
            curr = [0]*10
            for v in range(10):
                add = best_val if v != best_idx else second_best
                curr[v] = freq[j][v] + add
            prev = curr
        max_match = max(prev)
        return m*n - max_match
