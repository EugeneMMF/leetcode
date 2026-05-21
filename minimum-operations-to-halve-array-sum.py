import heapq
from typing import List

class Solution:
    def halveArray(self, nums: List[int]) -> int:
        total = sum(nums)
        target = total / 2
        max_heap = [-x for x in nums]
        heapq.heapify(max_heap)
        ops = 0
        current = total
        while current > target:
            largest = -heapq.heappop(max_heap)
            reduced = largest / 2
            current -= largest - reduced
            heapq.heappush(max_heap, -reduced)
            ops += 1
        return ops
