class SmallestInfiniteSet:

    def __init__(self):
        import heapq
        self.next = 1
        self.heap = []
        self.in_heap = set()

    def popSmallest(self) -> int:
        import heapq
        if self.heap:
            val = heapq.heappop(self.heap)
            self.in_heap.remove(val)
            return val
        else:
            val = self.next
            self.next += 1
            return val

    def addBack(self, num: int) -> None:
        import heapq
        if num < self.next and num not in self.in_heap:
            heapq.heappush(self.heap, num)
            self.in_heap.add(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
