class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        import sys
        sys.setrecursionlimit(200000)
        n = len(amount)
        adj = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        parent = [-1] * n
        depth = [0] * n
        stack = [0]
        parent[0] = -1
        while stack:
            u = stack.pop()
            for v in adj[u]:
                if v == parent[u]:
                    continue
                parent[v] = u
                depth[v] = depth[u] + 1
                stack.append(v)
        INF = 10**9
        bob_time = [INF] * n
        cur = bob
        while cur != -1:
            bob_time[cur] = depth[bob] - depth[cur]
            cur = parent[cur]
        best = -INF
        def dfs(u, cur_sum):
            nonlocal best
            contrib = 0
            if bob_time[u] > depth[u]:
                contrib = amount[u]
            elif bob_time[u] == depth[u]:
                contrib = amount[u] // 2
            cur_sum += contrib
            if len(adj[u]) == 1 and u != 0:
                best = max(best, cur_sum)
                return
            for v in adj[u]:
                if v == parent[u]:
                    continue
                dfs(v, cur_sum)
        dfs(0, 0)
        return best