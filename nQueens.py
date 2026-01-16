from typing import List
from copy import deepcopy

# class Solution:
#   def solveNQueens(self, n: int) -> List[List[str]]:
#     def prune(play: tuple[int,int], initial: dict):
#       r,c = play
#       # remove the row and columns
#       for i in range(n):
#         initial.pop((r,i), 0)
#         initial.pop((i,c), 0)
#       # remove the diagonals
#       for k in range(-min(r,c), n - max(r,c)):
#         initial.pop((r+k,c+k), 0)
#       for k in range(1, min(n-r-1, c)+1):
#         initial.pop((r+k,c-k), 0)
#       for k in range(1, min(n-c-1, r)+1):
#         initial.pop((r-k,c+k), 0)

#     results = []
#     playable = {}
#     for r in range(n):
#       for c in range(n):
#         playable[(r,c)] = 0
#     queens_series = []
#     for i in range(n):
#       playable.pop((0,i))
#       queens = set()
#       queens.add((0,i))
#       playable_series = []
#       temp_playable = playable.copy()
#       playable_series.append(playable.copy())
#       queens_series.append(queens.copy())
#       prune((0,i), temp_playable)
#       if len(queens) == n:
#         results.append(queens)
#         break
#       level = 1
#       while len(playable_series):
#         while len(temp_playable):
#           play = list(temp_playable.keys())[0]
#           temp_playable.pop(play)
#           playable_series.append(temp_playable.copy())
#           queens_series.append(queens.copy())
#           if play[0] != level:
#             level = len(playable_series)
#             temp_playable = playable_series.pop()
#             queens = queens_series.pop()
#             continue
#           queens.add(play)
#           prune(play, temp_playable)
#           level += 1
#           if len(queens) == n:
#             results.append(queens.copy())
#             level = len(playable_series)
#         temp_playable = playable_series.pop()
#         queens = queens_series.pop()
#         # print(list(temp_playable.keys()))
#         level = len(playable_series)
#     temp_res = []
#     for res in results:
#       mod = [["."]*n for _ in range(n)]
#       for i,j in res:
#         mod[i][j] = "Q"
#       temp_res.append(["".join(t) for t in mod])
#     return temp_res

def printBoard(board):
  [print(" ".join(row)) for row in board]

class Solution:
  def solveNQueens(self, n: int) -> List[List[str]]:
    def eliminate(play: tuple[int,int], board: dict):
      r,c = play
      for i in range(n):
        board[r][i] = "x"
        board[i][c] = "x"
      for i in range(-min(r,c), min(n-r,n-c)):
        board[r+i][c+i] = "x"
      for i in range(min(c+1,n-r)):
        board[r+i][c-i] = "x"
      for i in range(min(n-c,r+1)):
        board[r-i][c+i] = "x"
      board[r][c] = "Q"
      # printBoard(board)

    def trySolutions(board: List[str], n: int):
      if n == 0: return True
      solutions = []
      for c,option in enumerate(board[n-1]):
        if option == ".":
          board_copy = deepcopy(board)
          eliminate((n-1,c), board_copy)
          temp = trySolutions(board_copy, n-1)
          if temp == True:
            solutions.append(["".join(row).replace("x", ".") for row in board_copy])
          elif isinstance(temp, list):
            temp = [["".join(row).replace("x", ".") for row in temp1] for temp1 in temp]
            solutions.extend(temp)
      return solutions

    board = [["."]*n for _ in range(n)]
    return len(trySolutions(board, n))

print((Solution().solveNQueens(1)))