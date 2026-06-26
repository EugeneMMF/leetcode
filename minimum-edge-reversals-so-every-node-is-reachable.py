class Solution:
    def minEdgeReversals(self, n: int, edges: List[List[int]]) -> List[int]:
        import sys
        sys.setrecursionlimit(2 * n + 10)
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append((v, 0))
            adj[v].append((u, 1))
        ans = [0] * n
        initial = 0

        def dfs(u, p):
            nonlocal initial
            for v, w in adj[u]:
                if v == p:
                    continue
                initial += w
                dfs(v, u)

        dfs(0, -1)
        ans[0] = initial

        def dfs2(u, p):
            for v, w in adj[u]:
                if v == p:
                    continue
                ans[v] = ans[u] + (1 - 2 * w)
                dfs2(v, u)

        dfs2(0, -1)
        return ans
