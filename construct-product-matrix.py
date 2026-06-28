class Solution:
    def constructProductMatrix(self, grid):
        mod = 12345
        n = len(grid)
        m = len(grid[0])
        k = n * m
        vals = [0] * k
        idx = 0
        for i in range(n):
            row = grid[i]
            for j in range(m):
                vals[idx] = row[j] % mod
                idx += 1
        prefix = [0] * k
        suffix = [0] * k
        prefix[0] = vals[0]
        for i in range(1, k):
            prefix[i] = (prefix[i-1] * vals[i]) % mod
        suffix[k-1] = vals[k-1]
        for i in range(k-2, -1, -1):
            suffix[i] = (suffix[i+1] * vals[i]) % mod
        res = [[0] * m for _ in range(n)]
        idx = 0
        for i in range(n):
            for j in range(m):
                if idx == 0:
                    prod = suffix[1]
                elif idx == k-1:
                    prod = prefix[k-2]
                else:
                    prod = (prefix[idx-1] * suffix[idx+1]) % mod
                res[i][j] = prod
                idx += 1
        return res