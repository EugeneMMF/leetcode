class Solution:
    def mincostToHireWorkers(self, quality, wage, k):
        workers = sorted([(w / q, q) for q, w in zip(quality, wage)])
        import heapq
        heap = []
        sum_q = 0
        best = float('inf')
        for ratio, q in workers:
            heapq.heappush(heap, -q)
            sum_q += q
            if len(heap) > k:
                sum_q += heapq.heappop(heap)
            if len(heap) == k:
                cost = sum_q * ratio
                if cost < best:
                    best = cost
        return best
