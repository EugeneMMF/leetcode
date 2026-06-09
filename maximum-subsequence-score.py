class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        import heapq
        indices = sorted(range(len(nums1)), key=lambda i: nums2[i], reverse=True)
        heap = []
        total = 0
        best = 0
        for i in indices:
            val = nums1[i]
            total += val
            heapq.heappush(heap, val)
            if len(heap) > k:
                removed = heapq.heappop(heap)
                total -= removed
            if len(heap) == k:
                best = max(best, total * nums2[i])
        return best
