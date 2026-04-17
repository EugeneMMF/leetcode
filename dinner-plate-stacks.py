class DinnerPlates:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.stacks = []
        self.min_heap = []
        self.max_heap = []

    def push(self, val: int) -> None:
        while self.min_heap and (self.min_heap[0] >= len(self.stacks) or len(self.stacks[self.min_heap[0]]) >= self.capacity):
            import heapq
            heapq.heappop(self.min_heap)
        if not self.min_heap:
            idx = len(self.stacks)
            self.stacks.append([])
        else:
            import heapq
            idx = heapq.heappop(self.min_heap)
        self.stacks[idx].append(val)
        import heapq
        if len(self.stacks[idx]) < self.capacity:
            heapq.heappush(self.min_heap, idx)
        heapq.heappush(self.max_heap, -idx)

    def pop(self) -> int:
        import heapq
        while self.max_heap:
            idx = -heapq.heappop(self.max_heap)
            if idx < len(self.stacks) and self.stacks[idx]:
                val = self.stacks[idx].pop()
                if len(self.stacks[idx]) < self.capacity:
                    heapq.heappush(self.min_heap, idx)
                if self.stacks[idx]:
                    heapq.heappush(self.max_heap, -idx)
                return val
        return -1

    def popAtStack(self, index: int) -> int:
        import heapq
        if index >= len(self.stacks) or not self.stacks[index]:
            return -1
        val = self.stacks[index].pop()
        if len(self.stacks[index]) < self.capacity:
            heapq.heappush(self.min_heap, index)
        if self.stacks[index]:
            heapq.heappush(self.max_heap, -index)
        return val

# Your DinnerPlates object will be instantiated and called as such:
# obj = DinnerPlates(capacity)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAtStack(index)
