from typing import List
import heapq

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        qs = sorted([(q, i) for i, q in enumerate(queries)])
        intervals.sort(key=lambda x: x[0])
        res = [-1] * len(queries)
        heap = []
        idx = 0
        for q, qi in qs:
            while idx < len(intervals) and intervals[idx][0] <= q:
                l, r = intervals[idx]
                heapq.heappush(heap, (r - l + 1, r))
                idx += 1
            while heap and heap[0][1] < q:
                heapq.heappop(heap)
            if heap:
                res[qi] = heap[0][0]
        return res
