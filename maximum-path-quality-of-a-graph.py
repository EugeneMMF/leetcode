class Solution:
    def maximalPathQuality(self, values: List[int], edges: List[List[int]], maxTime: int) -> int:
        n = len(values)
        adj = [[] for _ in range(n)]
        for u, v, t in edges:
            adj[u].append((v, t))
            adj[v].append((u, t))
        best = 0
        visited = set([0])
        def dfs(node, time, cur_val):
            nonlocal best
            if node == 0:
                best = max(best, cur_val)
            if time == maxTime:
                return
            for nxt, w in adj[node]:
                if time + w > maxTime:
                    continue
                if nxt not in visited:
                    visited.add(nxt)
                    dfs(nxt, time + w, cur_val + values[nxt])
                    visited.remove(nxt)
                else:
                    dfs(nxt, time + w, cur_val)
        dfs(0, 0, values[0])
        return best