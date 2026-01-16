from typing import List

class Solution:
  def rotate(self, matrix: List[List[int]]) -> None:
    def switch(a, b, c, d):
      for i in range(len(a)):
        temp = matrix[d[i][0]][d[i][1]]
        matrix[d[i][0]][d[i][1]] = matrix[c[i][0]][c[i][1]]
        matrix[c[i][0]][c[i][1]] = matrix[b[i][0]][b[i][1]]
        matrix[b[i][0]][b[i][1]] = matrix[a[i][0]][a[i][1]]
        matrix[a[i][0]][a[i][1]] = temp

    end = len(matrix) - 1
    start = 0
    while end - start > 0:
      a = []
      b = []
      c = []
      d = []
      i = start
      j = start
      while j < end:
        a.append((i,j))
        j+=1
      while i < end:
        b.append((i,j))
        i += 1
      while j > start:
        c.append((i,j))
        j -= 1
      while i > start:
        d.append((i,j))
        i -= 1
      switch(a,b,c,d)
      end -= 1
      start += 1