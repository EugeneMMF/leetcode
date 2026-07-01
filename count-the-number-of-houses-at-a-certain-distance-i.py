class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        from collections import deque
        adj = [[] for _ in range(n + 1)]
        for i in range(1, n):
            adj[i].append(i + 1)
            adj[i + 1].append(i)
        if x != y:
            adj[x].append(y)
            adj[y].append(x)
        result = [0] * (n + 1)
        for start in range(1, n + 1):
            dist = [-1] * (n + 1)
            q = deque([start])
            dist[start] = 0
            while q:
                u = q.popleft()
                for v in adj[u]:
                    if dist[v] == -1:
                        dist[v] = dist[u] + 1
                        q.append(v)
            for end in range(1, n + 1):
                if start != end:
                    d = dist[end]
                    if d > 0:
                        result[d] += 1
        return result[1:]
