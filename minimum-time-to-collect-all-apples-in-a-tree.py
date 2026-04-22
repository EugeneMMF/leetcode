class Solution:
    def minTime(self, n, edges, hasApple):
        adj = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        import sys
        sys.setrecursionlimit(2000000)
        visited = [False] * n
        def dfs(u):
            visited[u] = True
            total = 0
            for v in adj[u]:
                if not visited[v]:
                    child = dfs(v)
                    if child > 0 or hasApple[v]:
                        total += child + 2
            return total
        return dfs(0)
