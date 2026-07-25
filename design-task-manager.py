class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        import heapq
        self.heap = []
        self.task_info = {}
        for userId, taskId, priority in tasks:
            self.task_info[taskId] = (userId, priority)
            heapq.heappush(self.heap, (-priority, -taskId, taskId))

    def add(self, userId: int, taskId: int, priority: int) -> None:
        import heapq
        self.task_info[taskId] = (userId, priority)
        heapq.heappush(self.heap, (-priority, -taskId, taskId))

    def edit(self, taskId: int, newPriority: int) -> None:
        import heapq
        userId, _ = self.task_info[taskId]
        self.task_info[taskId] = (userId, newPriority)
        heapq.heappush(self.heap, (-newPriority, -taskId, taskId))

    def rmv(self, taskId: int) -> None:
        del self.task_info[taskId]

    def execTop(self) -> int:
        import heapq
        while self.heap:
            neg_priority, neg_taskId, taskId = heapq.heappop(self.heap)
            if taskId in self.task_info:
                userId, priority = self.task_info[taskId]
                if priority == -neg_priority:
                    del self.task_info[taskId]
                    return userId
        return -1

# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()