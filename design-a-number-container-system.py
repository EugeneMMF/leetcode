class NumberContainers:

    def __init__(self):
        self.idx_num = {}
        self.num_idx_set = {}
        self.num_idx_heap = {}

    def change(self, index: int, number: int) -> None:
        old = self.idx_num.get(index)
        if old is not None:
            if old == number:
                return
            s = self.num_idx_set[old]
            s.discard(index)
            if not s:
                del self.num_idx_set[old]
        self.idx_num[index] = number
        if number not in self.num_idx_set:
            self.num_idx_set[number] = set()
            self.num_idx_heap[number] = []
        self.num_idx_set[number].add(index)
        import heapq
        heapq.heappush(self.num_idx_heap[number], index)

    def find(self, number: int) -> int:
        if number not in self.num_idx_set or not self.num_idx_set[number]:
            return -1
        heap = self.num_idx_heap[number]
        import heapq
        while heap and heap[0] not in self.num_idx_set[number]:
            heapq.heappop(heap)
        if not heap:
            return -1
        return heap[0]