class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        import heapq, math
        max_heap = [-g for g in gifts]
        heapq.heapify(max_heap)
        for _ in range(k):
            val = -heapq.heappop(max_heap)
            new_val = math.isqrt(val)
            heapq.heappush(max_heap, -new_val)
        return -sum(max_heap)
