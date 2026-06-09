class Solution:
    def isPossible(self, n: int, edges: List[List[int]]) -> bool:
        adj = [set() for _ in range(n + 1)]
        deg = [0] * (n + 1)
        for u, v in edges:
            adj[u].add(v)
            adj[v].add(u)
            deg[u] += 1
            deg[v] += 1
        odds = [i for i in range(1, n + 1) if deg[i] % 2 == 1]
        k = len(odds)
        if k == 0:
            return True
        if k == 2:
            a, b = odds
            if b not in adj[a]:
                return True
            for c in range(1, n + 1):
                if c == a or c == b:
                    continue
                if c not in adj[a] and c not in adj[b]:
                    return True
            return False
        if k == 4:
            a, b, c, d = odds
            pairs = [((a, b), (c, d)), ((a, c), (b, d)), ((a, d), (b, c))]
            for (x, y), (u, v) in pairs:
                if y not in adj[x] and v not in adj[u]:
                    return True
            return False
        return False