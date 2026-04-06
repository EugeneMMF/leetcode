class Solution:
    def tictactoe(self, moves: list[list[int]]) -> str:
        grid = [[' '] * 3 for _ in range(3)]
        
        for i, move in enumerate(moves):
            r, c = move
            
            player_char = 'X' if i % 2 == 0 else 'O'
            grid[r][c] = player_char
            
            for row_idx in range(3):
                if grid[row_idx][0] == grid[row_idx][1] == grid[row_idx][2] == player_char:
                    return "A" if player_char == 'X' else "B"
            
            for col_idx in range(3):
                if grid[0][col_idx] == grid[1][col_idx] == grid[2][col_idx] == player_char:
                    return "A" if player_char == 'X' else "B"
            
            if grid[0][0] == grid[1][1] == grid[2][2] == player_char:
                return "A" if player_char == 'X' else "B"
            
            if grid[0][2] == grid[1][1] == grid[2][0] == player_char:
                return "A" if player_char == 'X' else "B"
                
        if len(moves) == 9:
            return "Draw"
        else:
            return "Pending"
