from typing import List

class Node:
  def __init__(self):
    self.next = {}
    self.word = None

class Solution:
  def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
    m,n = len(board)-1, len(board[0])-1
    result = []

    def dfs(i, j, node):
      char = board[i][j]
      if char == '#' or char not in node.next: return
      node = node.next[char]
      if node.word != None:
        result.append(node.word)
        node.word = None
      board[i][j] = '#'  # Mark the route you have taken so far
      if i > 0: dfs(i-1, j, node)
      if j > 0: dfs(i, j-1, node)
      if i < m: dfs(i+1, j, node)
      if j < n: dfs(i, j+1, node)
      board[i][j] = char

    root = Node()
    for word in words:
      node = root
      for char in word:
        if char not in node.next:
          node.next[char] = Node()
        node = node.next[char]
      node.word = word

    for i in range(m+1):
      for j in range(n+1):
        dfs(i, j, root)
    return result