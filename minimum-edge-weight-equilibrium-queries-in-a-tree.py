class Solution:
    def minOperationsQueries(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        from collections import defaultdict, deque
        LOG = (n-1).bit_length()
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))
        parent = [[-1]*n for _ in range(LOG)]
        depth = [0]*n
        freq = [[0]*27 for _ in range(n)]
        stack = [0]
        visited = [False]*n
        visited[0] = True
        while stack:
            u = stack.pop()
            for v, w in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    parent[0][v] = u
                    depth[v] = depth[u] + 1
                    freq[v] = freq[u][:]  # copy
                    freq[v][w] += 1
                    stack.append(v)
        for k in range(1, LOG):
            for v in range(n):
                if parent[k-1][v] != -1:
                    parent[k][v] = parent[k-1][parent[k-1][v]]
        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u
            diff = depth[u] - depth[v]
            bit = 0
            while diff:
                if diff & 1:
                    u = parent[bit][u]
                diff >>= 1
                bit += 1
            if u == v:
                return u
            for k in range(LOG-1, -1, -1):
                if parent[k][u] != -1 and parent[k][u] != parent[k][v]:
                    u = parent[k][u]
                    v = parent[k][v]
            return parent[0][u]
        res = []
        for a, b in queries:
            if a == b:
                res.append(0)
                continue
            L = lca(a, b)
            path_len = depth[a] + depth[b] - 2*depth[L]
            maxf = 0
            for w in range(1, 27):
                cnt = freq[a][w] + freq[b][w] - 2*freq[L][w]
                if cnt > maxf:
                    maxf = cnt
            res.append(path_len - maxf)
        return res