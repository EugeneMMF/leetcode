class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        forbidden_set = set(forbidden)
        limit = max(max(forbidden, default=0) + a + b, x + a + b) + 2000
        visited = set()
        q = deque()
        q.append((0, False, 0))
        visited.add((0, False))
        while q:
            pos, prev_back, steps = q.popleft()
            if pos == x:
                return steps
            forward = pos + a
            if forward <= limit and forward not in forbidden_set and (forward, False) not in visited:
                visited.add((forward, False))
                q.append((forward, False, steps + 1))
            if not prev_back:
                backward = pos - b
                if backward >= 0 and backward not in forbidden_set and (backward, True) not in visited:
                    visited.add((backward, True))
                    q.append((backward, True, steps + 1))
        return -1
