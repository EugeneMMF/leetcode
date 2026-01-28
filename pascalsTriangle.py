from typing import List

class Solution:
  def generate(self, numRows: int) -> List[List[int]]:
    answer = [[1]]
    if numRows == 1: return answer
    answer.append([1,1])
    for i in range(2, numRows):
      tmp = [1]
      for j in range(i-1):
        tmp.append(answer[i-1][j] + answer[i-1][j+1])
      tmp.append(1)
      answer.append(tmp)
    return answer