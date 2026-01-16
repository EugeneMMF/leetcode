import heapq
from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        grids = [[set() for _ in range(3)] for _ in range(3)]
        empty_cells = []
        for i, row in enumerate(board):
            for j, number in enumerate(row):
                if number == ".":
                    empty_cells.append((i, j))
                else:
                    rows[i].add(number)
                    cols[j].add(number)
                    grids[i//3][j//3].add(number)

        empty_cells = [
            (i, j)
            for i, j in empty_cells
        ]
        heapq.heapify(empty_cells)

        def try_fill_board():
            if not empty_cells:
                return True

            i, j = heapq.heappop(empty_cells)
            row = rows[i]
            col = cols[j]
            grid = grids[i//3][j//3]
            for number in '123456789':
                if (number in row or number in col or number in grid):
                    continue
                board[i][j] = number
                row.add(number)
                col.add(number)
                grid.add(number)

                if try_fill_board():
                    return True

                row.remove(number)
                col.remove(number)
                grid.remove(number)

            heapq.heappush(empty_cells, (i, j))
            return False

        try_fill_board()