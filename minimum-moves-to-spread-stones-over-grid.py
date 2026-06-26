class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        stones = []
        for i in range(3):
            for j in range(3):
                stones.extend([(i, j)] * grid[i][j])
        targets = [(i, j) for i in range(3) for j in range(3)]
        n = 9
        cost = [[0]*n for _ in range(n)]
        for i in range(n):
            si, sj = stones[i]
            for j in range(n):
                ti, tj = targets[j]
                cost[i][j] = abs(si - ti) + abs(sj - tj)
        INF = 10**9
        dp = [INF]*(1<<n)
        dp[0] = 0
        for mask in range(1<<n):
            k = bin(mask).count('1')
            if k == n:
                continue
            for j in range(n):
                if not (mask>>j)&1:
                    newmask = mask | (1<<j)
                    val = dp[mask] + cost[k][j]
                    if val < dp[newmask]:
                        dp[newmask] = val
        return dp[(1<<n)-1]
