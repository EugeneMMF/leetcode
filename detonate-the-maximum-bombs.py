class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        adj = [[] for _ in range(n)]
        for i in range(n):
            xi, yi, ri = bombs[i]
            for j in range(n):
                if i == j:
                    continue
                xj, yj, _ = bombs[j]
                if (xj - xi) ** 2 + (yj - yi) ** 2 <= ri ** 2:
                    adj[i].append(j)
        max_count = 0
        for i in range(n):
            seen = [False] * n
            stack = [i]
            seen[i] = True
            count = 0
            while stack:
                u = stack.pop()
                count += 1
                for v in adj[u]:
                    if not seen[v]:
                        seen[v] = True
                        stack.append(v)
            max_count = max(max_count, count)
        return max_count
