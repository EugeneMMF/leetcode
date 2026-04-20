from typing import List
import heapq

class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort(key=lambda x: x[0])
        i, n = 0, len(events)
        day = 0
        res = 0
        heap = []
        while i < n or heap:
            if not heap:
                day = events[i][0]
            while i < n and events[i][0] <= day:
                heapq.heappush(heap, events[i][1])
                i += 1
            while heap and heap[0] < day:
                heapq.heappop(heap)
            if heap:
                heapq.heappop(heap)
                res += 1
                day += 1
        return res
