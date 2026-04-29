from typing import List
import heapq

class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        heap = []
        min_val = float('inf')
        for x in nums:
            if x % 2:
                x *= 2
            heapq.heappush(heap, -x)
            if x < min_val:
                min_val = x
        ans = float('inf')
        while True:
            max_val = -heap[0]
            if max_val - min_val < ans:
                ans = max_val - min_val
            if max_val % 2:
                break
            heapq.heappop(heap)
            new_val = max_val // 2
            heapq.heappush(heap, -new_val)
            if new_val < min_val:
                min_val = new_val
        return ans
