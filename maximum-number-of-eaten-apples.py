class Solution:
    def eatenApples(self, apples, days):
        import heapq
        heap = []
        i = 0
        n = len(apples)
        eaten = 0
        day = 0
        while i < n or heap:
            if i < n and apples[i] > 0:
                heapq.heappush(heap, (day + days[i], apples[i]))
            while heap and heap[0][0] <= day:
                heapq.heappop(heap)
            if heap:
                expire, cnt = heapq.heappop(heap)
                cnt -= 1
                eaten += 1
                if cnt > 0:
                    heapq.heappush(heap, (expire, cnt))
            day += 1
            i += 1
        return eaten
