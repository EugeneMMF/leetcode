class Solution:
    def updateBoard(self, board: list[list[str]], click: list[int]) -> list[list[str]]:
        m, n = len(board), len(board[0])
        clickr, clickc = click[0], click[1]

        if board[clickr][clickc] == 'M':
            board[clickr][clickc] = 'X'
            return board

        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1), (1, 0), (1, 1)
        ]

        def dfs(r, c):
            if not (0 <= r < m and 0 <= c < n) or board[r][c] != 'E':
                return

            mine_count = 0
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and board[nr][nc] == 'M':
                    mine_count += 1

            if mine_count == 0:
                board[r][c] = 'B'
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and board[nr][nc] == 'E':
                        dfs(nr, nc)
            else:
                board[r][c] = str(mine_count)

        dfs(clickr, clickc)

        return board
