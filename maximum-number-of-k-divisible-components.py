class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        import sys
        sys.setrecursionlimit(1 << 25)
        g = [[] for _ in range(n)]
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)
        cnt = 0
        def dfs(u, p):
            nonlocal cnt
            total = values[u] % k
            for v in g[u]:
                if v == p:
                    continue
                sub = dfs(v, u)
                total = (total + sub) % k
            if total == 0:
                if u != 0:
                    cnt += 1
                return 0
            return total
        dfs(0, -1)
        return cnt + 1