class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        import heapq
        heap = [-x for x in nums]
        heapq.heapify(heap)
        score = 0
        for _ in range(k):
            max_val = -heapq.heappop(heap)
            score += max_val
            new_val = (max_val + 2) // 3
            heapq.heappush(heap, -new_val)
        return score