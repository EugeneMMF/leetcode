class Solution:
    def countBattleships(self, board: list[list[str]]) -> int:
        m = len(board)
        if m == 0:
            return 0
        n = len(board[0])

        count = 0
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'X':
                    is_top_of_ship = (i == 0 or board[i-1][j] == '.')
                    is_left_of_ship = (j == 0 or board[i][j-1] == '.')
                    
                    if is_top_of_ship and is_left_of_ship:
                        count += 1
        return count
