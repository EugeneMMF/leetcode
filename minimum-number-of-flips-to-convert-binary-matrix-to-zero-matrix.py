import collections

class Solution:
    def minFlips(self, mat: list[list[int]]) -> int:
        m = len(mat)
        n = len(mat[0])

        initial_state = tuple(tuple(row) for row in mat)
        target_state = tuple(tuple(0 for _ in range(n)) for _ in range(m))

        q = collections.deque([(initial_state, 0)])
        visited = {initial_state}

        dr = [-1, 1, 0, 0]
        dc = [0, 0, -1, 1]

        while q:
            current_mat_tuple, steps = q.popleft()

            if current_mat_tuple == target_state:
                return steps

            current_mat = [list(row) for row in current_mat_tuple]

            for r in range(m):
                for c in range(n):
                    next_mat = [row[:] for row in current_mat]

                    next_mat[r][c] ^= 1
                    
                    for i in range(4):
                        nr, nc = r + dr[i], c + dc[i]
                        if 0 <= nr < m and 0 <= nc < n:
                            next_mat[nr][nc] ^= 1

                    next_mat_tuple = tuple(tuple(row) for row in next_mat)

                    if next_mat_tuple not in visited:
                        visited.add(next_mat_tuple)
                        q.append((next_mat_tuple, steps + 1))
        
        return -1

