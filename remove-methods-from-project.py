class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        from collections import deque
        adj = [[] for _ in range(n)]
        for a, b in invocations:
            adj[a].append(b)
        is_suspicious = [False] * n
        q = deque([k])
        is_suspicious[k] = True
        while q:
            u = q.popleft()
            for v in adj[u]:
                if not is_suspicious[v]:
                    is_suspicious[v] = True
                    q.append(v)
        possible = True
        for a, b in invocations:
            if is_suspicious[b] and not is_suspicious[a]:
                possible = False
                break
        if not possible:
            return list(range(n))
        return [i for i in range(n) if not is_suspicious[i]]