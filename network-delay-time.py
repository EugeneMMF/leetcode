import collections
import heapq
import math

class Solution:
    def networkDelayTime(self, times, n, k):
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        dist = {i: math.inf for i in range(1, n + 1)}
        dist[k] = 0

        pq = [(0, k)]

        while pq:
            current_time, u = heapq.heappop(pq)

            if current_time > dist[u]:
                continue

            for v, travel_time in graph[u]:
                new_time = current_time + travel_time
                if new_time < dist[v]:
                    dist[v] = new_time
                    heapq.heappush(pq, (new_time, v))
        
        max_delay = 0
        for node in range(1, n + 1):
            if dist[node] == math.inf:
                return -1
            max_delay = max(max_delay, dist[node])
        
        return max_delay
