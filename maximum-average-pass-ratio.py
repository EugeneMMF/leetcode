import heapq
from typing import List

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        heap = []
        for p, t in classes:
            delta = (t - p) / (t * (t + 1))
            heapq.heappush(heap, (-delta, p, t))
        for _ in range(extraStudents):
            neg_delta, p, t = heapq.heappop(heap)
            p += 1
            t += 1
            delta = (t - p) / (t * (t + 1))
            heapq.heappush(heap, (-delta, p, t))
        total = 0.0
        while heap:
            _, p, t = heapq.heappop(heap)
            total += p / t
        return total / len(classes)
