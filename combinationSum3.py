from typing import List

class Solution:
  def combinationSum3(self, k: int, n: int) -> List[List[int]]:
    results = []
    def find(i, values, sm):
      if len(values) == k and sm == n:
        results.append(values.copy())
        return
      if i <= 9:
        values.append(i)
        find(i+1, values, sm+i)
        values.pop()
        find(i+1, values, sm)

    find(1, [], 0)
    return results