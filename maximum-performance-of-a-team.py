class Solution:
    def maxPerformance(self, n, speed, efficiency, k):
        engineers = list(zip(efficiency, speed))
        engineers.sort(reverse=True)
        import heapq
        heap = []
        sum_speed = 0
        max_perf = 0
        MOD = 10**9 + 7
        for eff, spd in engineers:
            if len(heap) == k:
                sum_speed -= heapq.heappop(heap)
            heapq.heappush(heap, spd)
            sum_speed += spd
            perf = sum_speed * eff
            if perf > max_perf:
                max_perf = perf
        return max_perf % MOD
