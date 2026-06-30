class Solution:
    def minimumOperationsToMakeEqual(self, x: int, y: int) -> int:
        if x == y:
            return 0
        from collections import deque
        q = deque()
        q.append((x, 0))
        visited = set([x])
        limit = max(x, y) * 2 + 10
        while q:
            cur, d = q.popleft()
            for nxt in ((cur - 1), (cur + 1)):
                if nxt == y:
                    return d + 1
                if 0 <= nxt <= limit and nxt not in visited:
                    visited.add(nxt)
                    q.append((nxt, d + 1))
            if cur % 11 == 0:
                nxt = cur // 11
                if nxt == y:
                    return d + 1
                if nxt not in visited:
                    visited.add(nxt)
                    q.append((nxt, d + 1))
            if cur % 5 == 0:
                nxt = cur // 5
                if nxt == y:
                    return d + 1
                if nxt not in visited:
                    visited.add(nxt)
                    q.append((nxt, d + 1))
        return -1