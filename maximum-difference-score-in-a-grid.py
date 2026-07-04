class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        INF = 10**10
        prefix = [[INF]*n for _ in range(m)]
        best = -10**10
        for i in range(m):
            for j in range(n):
                min_excl = INF
                if i>0:
                    min_excl = min(min_excl, prefix[i-1][j])
                if j>0:
                    min_excl = min(min_excl, prefix[i][j-1])
                if min_excl!=INF:
                    best = max(best, grid[i][j]-min_excl)
                cur = grid[i][j]
                if i>0:
                    cur = min(cur, prefix[i-1][j])
                if j>0:
                    cur = min(cur, prefix[i][j-1])
                prefix[i][j] = cur
        return best
