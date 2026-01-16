from typing import List

class Solution:
  def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort(key=lambda x: x[0])
    finalIntervals = [intervals[0]]
    for i in intervals[1:]:
      if finalIntervals[-1][1] >= i[0]:
        finalIntervals[-1][1] = max(i[1], finalIntervals[-1][1])
      else:
        finalIntervals.append(i)
    return finalIntervals