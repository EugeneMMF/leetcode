class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        import heapq
        MOD = 10**9 + 7
        heap = nums[:]
        heapq.heapify(heap)
        for _ in range(k):
            val = heapq.heappop(heap) + 1
            heapq.heappush(heap, val)
        prod = 1
        while heap:
            prod = (prod * heapq.heappop(heap)) % MOD
        return prod