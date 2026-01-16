from typing import List

class Solution:
  def exist(self, board: List[List[str]], word: str) -> bool:
    def getNeighbors(r,c,m,n):
      neighbors = []
      if r != 0:
        neighbors.append((r-1,c))
      if r != m-1:
        neighbors.append((r+1,c))
      if c != 0:
        neighbors.append((r,c-1))
      if c != n-1:
        neighbors.append((r,c+1))
      return neighbors

    m,n = len(board), len(board[0])
    word = list(word)
    ln = len(word)
    count = 0
    current = []
    for i in range(m):
      for j in range(n):
        current = []
        options = []
        if board[i][j] == word[0]:
          current.append((i,j))
          count = 1
          options = []
          if ln == 1: return True
          neighbors = getNeighbors(i,j,m,n)
          for r,c in neighbors:
            if board[r][c] == word[count] and (r,c) not in current:
              if ln == 2: return True
              options.append((r,c,count+1))
          while len(options):
            r,c,count = options.pop()
            current = current[:count]
            current.append((r,c))
            if count == ln: return True
            neighbors = getNeighbors(r,c,m,n)
            for r,c in neighbors:
              if board[r][c] == word[count] and (r,c) not in current:
                options.append((r,c,count+1))
    return False

print(Solution().exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB"))