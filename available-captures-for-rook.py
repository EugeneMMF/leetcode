from typing import List

class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        for i in range(8):
            for j in range(8):
                if board[i][j] == 'R':
                    r, c = i, j
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        cnt = 0
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            while 0 <= nr < 8 and 0 <= nc < 8:
                if board[nr][nc] == 'B':
                    break
                if board[nr][nc] == 'p':
                    cnt += 1
                    break
                nr += dr
                nc += dc
        return cnt
