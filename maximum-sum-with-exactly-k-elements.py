class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        import heapq
        max_heap = [-x for x in nums]
        heapq.heapify(max_heap)
        score = 0
        for _ in range(k):
            m = -heapq.heappop(max_heap)
            score += m
            heapq.heappush(max_heap, -(m + 1))
        return score
