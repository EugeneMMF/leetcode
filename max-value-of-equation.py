class Solution:
    def findMaxValueOfEquation(self, points, k):
        import heapq
        heap = []
        max_val = -10**18
        xi0, yi0 = points[0]
        heapq.heappush(heap, (-(yi0 - xi0), xi0))
        for xj, yj in points[1:]:
            while heap and heap[0][1] < xj - k:
                heapq.heappop(heap)
            if heap:
                best = -heap[0][0]
                cur = best + yj + xj
                if cur > max_val:
                    max_val = cur
            heapq.heappush(heap, (-(yj - xj), xj))
        return max_val
