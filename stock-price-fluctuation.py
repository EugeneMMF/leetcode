import heapq

class StockPrice:
    def __init__(self):
        self.time_price = {}
        self.max_heap = []
        self.min_heap = []
        self.max_timestamp = 0

    def update(self, timestamp: int, price: int) -> None:
        self.time_price[timestamp] = price
        if timestamp > self.max_timestamp:
            self.max_timestamp = timestamp
        heapq.heappush(self.max_heap, (-price, timestamp))
        heapq.heappush(self.min_heap, (price, timestamp))

    def current(self) -> int:
        return self.time_price[self.max_timestamp]

    def maximum(self) -> int:
        while True:
            price, timestamp = self.max_heap[0]
            price = -price
            if self.time_price.get(timestamp) == price:
                return price
            heapq.heappop(self.max_heap)

    def minimum(self) -> int:
        while True:
            price, timestamp = self.min_heap[0]
            if self.time_price.get(timestamp) == price:
                return price
            heapq.heappop(self.min_heap)

# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()
