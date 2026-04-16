class Solution:
    def numSubmatrixSumTarget(self, matrix, target):
        m = len(matrix)
        n = len(matrix[0])
        ans = 0
        for top in range(m):
            col = [0] * n
            for bottom in range(top, m):
                for c in range(n):
                    col[c] += matrix[bottom][c]
                cur = 0
                cnt = {0: 1}
                for v in col:
                    cur += v
                    ans += cnt.get(cur - target, 0)
                    cnt[cur] = cnt.get(cur, 0) + 1
        return ans
