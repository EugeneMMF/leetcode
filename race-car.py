class Solution:
    def racecar(self, target: int) -> int:
        from collections import deque
        limit = target * 2
        visited = set()
        q = deque()
        q.append((0, 1, 0))
        visited.add((0, 1))
        while q:
            pos, speed, steps = q.popleft()
            if pos == target:
                return steps
            # Accelerate
            npos = pos + speed
            nspeed = speed * 2
            if -limit <= npos <= limit and (npos, nspeed) not in visited:
                visited.add((npos, nspeed))
                q.append((npos, nspeed, steps + 1))
            # Reverse
            rev_speed = -1 if speed > 0 else 1
            if (pos, rev_speed) not in visited:
                visited.add((pos, rev_speed))
                q.append((pos, rev_speed, steps + 1))
