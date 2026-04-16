class Solution:
    def isEscapePossible(self, blocked, source, target):
        if not blocked:
            return True
        B = set(map(tuple, blocked))
        limit = len(blocked) * (len(blocked) - 1) // 2
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        def bfs(start, finish):
            from collections import deque
            q = deque([tuple(start)])
            visited = {tuple(start)}
            while q and len(visited) <= limit:
                x, y = q.popleft()
                if [x, y] == finish:
                    return True
                for dx, dy in dirs:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < 10**6 and 0 <= ny < 10**6 and (nx, ny) not in B and (nx, ny) not in visited:
                        visited.add((nx, ny))
                        q.append((nx, ny))
            return len(visited) > limit
        return bfs(source, target) and bfs(target, source)
