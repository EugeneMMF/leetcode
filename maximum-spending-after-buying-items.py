class Solution:
    def maxSpending(self, values: List[List[int]]) -> int:
        import heapq
        m = len(values)
        n = len(values[0]) if m else 0
        idx = [n - 1] * m
        heap = []
        for i in range(m):
            heapq.heappush(heap, (values[i][idx[i]], i))
        total = 0
        for day in range(1, m * n + 1):
            val, i = heapq.heappop(heap)
            total += val * day
            idx[i] -= 1
            if idx[i] >= 0:
                heapq.heappush(heap, (values[i][idx[i]], i))
        return total