from typing import List
import heapq

class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        n = len(servers)
        m = len(tasks)
        free = [(servers[i], i) for i in range(n)]
        heapq.heapify(free)
        busy = []
        ans = [0] * m
        time = 0
        for j in range(m):
            time = max(time, j)
            while busy and busy[0][0] <= time:
                ft, w, idx = heapq.heappop(busy)
                heapq.heappush(free, (w, idx))
            if not free:
                time = busy[0][0]
                while busy and busy[0][0] <= time:
                    ft, w, idx = heapq.heappop(busy)
                    heapq.heappush(free, (w, idx))
            w, idx = heapq.heappop(free)
            ans[j] = idx
            finish = time + tasks[j]
            heapq.heappush(busy, (finish, w, idx))
        return ans