class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:
        if n == m:
            return 1
        self.best = n * m
        self.n = n
        self.m = m
        heights = [0] * m
        def dfs(cnt):
            if cnt >= self.best:
                return
            min_h = min(heights)
            if min_h == n:
                self.best = cnt
                return
            idx = heights.index(min_h)
            max_len = min(n - min_h, m - idx)
            for size in range(max_len, 0, -1):
                ok = True
                for j in range(idx, idx + size):
                    if heights[j] != min_h:
                        ok = False
                        break
                if not ok:
                    continue
                for j in range(idx, idx + size):
                    heights[j] += size
                dfs(cnt + 1)
                for j in range(idx, idx + size):
                    heights[j] -= size
        dfs(0)
        return self.best
