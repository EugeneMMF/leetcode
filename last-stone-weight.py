from typing import List
import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h = [-s for s in stones]
        heapq.heapify(h)
        while len(h) > 1:
            y = -heapq.heappop(h)
            x = -heapq.heappop(h)
            if x != y:
                heapq.heappush(h, -(y - x))
        return -h[0] if h else 0
