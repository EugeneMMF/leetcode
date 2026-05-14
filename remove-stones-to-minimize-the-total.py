class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        import heapq
        heap = [-x for x in piles]
        heapq.heapify(heap)
        for _ in range(k):
            largest = -heapq.heappop(heap)
            reduced = largest - largest // 2
            heapq.heappush(heap, -reduced)
        return sum(-x for x in heap)
