from typing import List

class Solution:
  def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    n = len(intervals)
    finalIntervals = []
    start = 0
    for i in range(n):
      if intervals[i][0] < newInterval[0]:
        finalIntervals.append(intervals[i])
        start = i + 1
      else:
        start = i
        break
    if start == 0:
      finalIntervals.append(newInterval)
      tempIntervals = intervals
    else:
      tempIntervals = [newInterval, *intervals[start:]]
    for i in tempIntervals:
      if finalIntervals[-1][1] >= i[0]:
        finalIntervals[-1][1] = max(i[1], finalIntervals[-1][1])
      else:
        finalIntervals.append(i)
    return finalIntervals

print(Solution().insert([[1,5]],[2,3]))