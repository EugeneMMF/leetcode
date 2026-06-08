class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        from collections import defaultdict, deque
        adj = defaultdict(list)
        for a, b, w in roads:
            adj[a].append((b, w))
            adj[b].append((a, w))
        visited = [False] * (n + 1)
        dq = deque([1])
        visited[1] = True
        min_w = 10**9 + 1
        while dq:
            u = dq.popleft()
            for v, w in adj[u]:
                if w < min_w:
                    min_w = w
                if not visited[v]:
                    visited[v] = True
                    dq.append(v)
        return min_w