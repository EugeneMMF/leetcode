class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        dp = [[set() for _ in range(n)] for _ in range(m)]
        if grid[0][0] == '(':
            dp[0][0].add(1)
        else:
            return False
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                cur_set = set()
                if i > 0:
                    for opens in dp[i-1][j]:
                        new_opens = opens + (1 if grid[i][j] == '(' else -1)
                        if new_opens >= 0:
                            cur_set.add(new_opens)
                if j > 0:
                    for opens in dp[i][j-1]:
                        new_opens = opens + (1 if grid[i][j] == '(' else -1)
                        if new_opens >= 0:
                            cur_set.add(new_opens)
                dp[i][j] = cur_set
        return 0 in dp[m-1][n-1]