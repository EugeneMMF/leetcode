class ExamRoom:
    def __init__(self, n: int):
        self.n = n
        self.occupied = []
        self.heap = []
        import heapq
        self.heapq = heapq
        # initial interval covering whole room
        self.heapq.heappush(self.heap, (-(n - 1), -1, n))

    def _distance(self, l, r):
        if l == -1:
            return r
        if r == self.n:
            return self.n - 1 - l
        return (r - l) // 2

    def _seat_in_interval(self, l, r):
        if l == -1:
            return 0
        if r == self.n:
            return self.n - 1
        return (l + r) // 2

    def seat(self) -> int:
        import bisect
        while True:
            negdist, l, r = self.heapq.heappop(self.heap)
            seat = self._seat_in_interval(l, r)
            # verify interval is still valid
            idx = bisect.bisect_left(self.occupied, seat)
            left = self.occupied[idx - 1] if idx > 0 else -1
            right = self.occupied[idx] if idx < len(self.occupied) else self.n
            if left == l and right == r:
                bisect.insort(self.occupied, seat)
                # push new intervals
                if l != seat:
                    self.heapq.heappush(self.heap, (-(self._distance(l, seat)), l, seat))
                if seat != r:
                    self.heapq.heappush(self.heap, (-(self._distance(seat, r)), seat, r))
                return seat
            # else discard and continue

    def leave(self, p: int) -> None:
        import bisect
        idx = bisect.bisect_left(self.occupied, p)
        self.occupied.pop(idx)
        left = self.occupied[idx - 1] if idx > 0 else -1
        right = self.occupied[idx] if idx < len(self.occupied) else self.n
        self.heapq.heappush(self.heap, (-(self._distance(left, right)), left, right))
