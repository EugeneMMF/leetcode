from typing import List

class Solution:
  def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    order:dict[int,set[int]] = {}
    solution = []
    for (second, first) in prerequisites:
      order[second] = order.get(second, set())
      order[second].add(first)
    toLookAt = set([i for i in range(numCourses) if not order.get(i, None)])
    while toLookAt:
      number = toLookAt.pop()
      if not order.get(number, None):
        solution.append(number)
        order.pop(number, None)
        for key in order.keys():
          order[key].discard(number)
          if not order[key]:
            toLookAt.add(key)
    if len(solution) == numCourses: return solution
    return []

print(Solution().findOrder(2, [[1,0]]))