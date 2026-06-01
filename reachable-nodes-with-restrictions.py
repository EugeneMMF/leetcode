class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        adj = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        restricted_set = set(restricted)
        visited = [False] * n
        stack = [0]
        visited[0] = True
        count = 0
        while stack:
            u = stack.pop()
            count += 1
            for v in adj[u]:
                if not visited[v] and v not in restricted_set:
                    visited[v] = True
                    stack.append(v)
        return count
