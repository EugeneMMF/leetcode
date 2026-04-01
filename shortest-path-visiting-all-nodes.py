from collections import deque

class Solution:
    def shortestPathLength(self, graph: list[list[int]]) -> int:
        n = len(graph)
        if n == 1:
            return 0

        all_visited_mask = (1 << n) - 1
        queue = deque()
        visited = set()

        for i in range(n):
            mask = 1 << i
            queue.append((i, mask, 0))
            visited.add((i, mask))

        while queue:
            node, mask, dist = queue.popleft()

            if mask == all_visited_mask:
                return dist

            for neighbor in graph[node]:
                new_mask = mask | (1 << neighbor)
                if (neighbor, new_mask) not in visited:
                    visited.add((neighbor, new_mask))
                    queue.append((neighbor, new_mask, dist + 1))

        return -1

