import collections

class Solution:
    def cutOffTree(self, forest: list[list[int]]) -> int:
        m = len(forest)
        n = len(forest[0])

        trees = []
        for r in range(m):
            for c in range(n):
                if forest[r][c] > 1:
                    trees.append((forest[r][c], r, c))
        
        trees.sort()

        def bfs(start_r, start_c, target_r, target_c) -> int:
            if start_r == target_r and start_c == target_c:
                return 0

            queue = collections.deque([(start_r, start_c, 0)])
            visited = set([(start_r, start_c)])
            
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

            while queue:
                r, c, steps = queue.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < m and 0 <= nc < n and forest[nr][nc] != 0 and (nr, nc) not in visited:
                        if nr == target_r and nc == target_c:
                            return steps + 1

                        visited.add((nr, nc))
                        queue.append((nr, nc, steps + 1))
            
            return -1
        
        total_steps = 0
        current_pos = (0, 0)
        
        if forest[0][0] == 0:
            return -1

        for height, target_r, target_c in trees:
            steps = bfs(current_pos[0], current_pos[1], target_r, target_c)
            
            if steps == -1:
                return -1

            total_steps += steps
            current_pos = (target_r, target_c)
        
        return total_steps
