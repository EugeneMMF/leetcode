class Solution:
    def minMovesToCaptureTheQueen(self, a: int, b: int, c: int, d: int, e: int, f: int) -> int:
        from collections import deque
        rook = (a-1, b-1)
        bishop = (c-1, d-1)
        queen = (e-1, f-1)
        dirs_rook = [(-1,0),(1,0),(0,-1),(0,1)]
        dirs_bishop = [(-1,-1),(-1,1),(1,-1),(1,1)]
        def in_board(r,c):
            return 0 <= r < 8 and 0 <= c < 8
        def generate_moves(pos, dirs, other):
            r,c = pos
            for dr,dc in dirs:
                nr, nc = r+dr, c+dc
                while in_board(nr,nc):
                    if (nr,nc) == other:
                        break
                    if (nr,nc) == queen:
                        yield (nr,nc, True)
                        break
                    yield (nr,nc, False)
                    nr += dr
                    nc += dc
        visited = set()
        q = deque()
        q.append((rook, bishop, 0))
        visited.add((rook, bishop))
        while q:
            rpos, bpos, moves = q.popleft()
            for nr,nc,capture in generate_moves(rpos, dirs_rook, bpos):
                if capture:
                    return moves+1
                new_state = ((nr,nc), bpos)
                if new_state not in visited:
                    visited.add(new_state)
                    q.append((new_state[0], new_state[1], moves+1))
            for nr,nc,capture in generate_moves(bpos, dirs_bishop, rpos):
                if capture:
                    return moves+1
                new_state = (rpos, (nr,nc))
                if new_state not in visited:
                    visited.add(new_state)
                    q.append((new_state[0], new_state[1], moves+1))
        return -1