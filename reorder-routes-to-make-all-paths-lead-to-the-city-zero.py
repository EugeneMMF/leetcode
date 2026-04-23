class Solution:
    def minReorder(self, n, connections):
        adj = [[] for _ in range(n)]
        for a, b in connections:
            adj[a].append((b, 1))
            adj[b].append((a, 0))
        ans = 0
        stack = [(0, -1)]
        while stack:
            node, parent = stack.pop()
            for nei, cost in adj[node]:
                if nei == parent:
                    continue
                ans += cost
                stack.append((nei, node))
        return ans
