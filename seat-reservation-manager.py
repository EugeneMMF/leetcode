class SeatManager:

    def __init__(self, n: int):
        import heapq
        self.available = list(range(1, n+1))
        heapq.heapify(self.available)

    def reserve(self) -> int:
        import heapq
        return heapq.heappop(self.available)

    def unreserve(self, seatNumber: int) -> None:
        import heapq
        heapq.heappush(self.available, seatNumber)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)
