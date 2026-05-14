class Solution:
    def checkMove(self, board: List[List[str]], rMove: int, cMove: int, color: str) -> bool:
        opp = 'B' if color == 'W' else 'W'
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        for dx, dy in dirs:
            x, y = rMove + dx, cMove + dy
            cntOpp = 0
            while 0 <= x < 8 and 0 <= y < 8:
                ch = board[x][y]
                if ch == '.':
                    break
                if ch == opp:
                    cntOpp += 1
                    x += dx
                    y += dy
                    continue
                if ch == color:
                    if cntOpp >= 1:
                        return True
                    break
                break
        return False
