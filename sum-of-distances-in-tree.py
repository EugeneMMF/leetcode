
import collections

class Solution:
    def sumOfDistancesInTree(self, n: int, edges: list[list[int]]) -> list[int]:
        adj = collections.defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        ans = [0] * n
        count = [0] * n

        def dfs1(u, p):
            count[u] = 1
            for v in adj[u]:
                if v == p:
                    continue
                dfs1(v, u)
                count[u] += count[v]
                ans[u] += ans[v] + count[v]

        def dfs2(u, p):
            for v in adj[u]:
                if v == p:
                    continue
                ans[v] = ans[u] - count[v] + (n - count[v])
                dfs2(v, u)

        dfs1(0, -1)
        dfs2(0, -1)

        return ans
