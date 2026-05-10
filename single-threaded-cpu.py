class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        import heapq
        tasks = sorted([(t[0], t[1], i) for i, t in enumerate(tasks)], key=lambda x: x[0])
        res = []
        heap = []
        time = 0
        i = 0
        n = len(tasks)
        while i < n or heap:
            while i < n and tasks[i][0] <= time:
                heapq.heappush(heap, (tasks[i][1], tasks[i][2]))
                i += 1
            if heap:
                p, idx = heapq.heappop(heap)
                time += p
                res.append(idx)
            else:
                time = tasks[i][0]
        return res
