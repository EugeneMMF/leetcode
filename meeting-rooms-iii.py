class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        import heapq
        meetings.sort(key=lambda x: x[0])
        available = list(range(n))
        heapq.heapify(available)
        busy = []
        counts = [0] * n
        for s, e in meetings:
            duration = e - s
            while busy and busy[0][0] <= s:
                end_time, room = heapq.heappop(busy)
                heapq.heappush(available, room)
            if not available:
                end_time, room = heapq.heappop(busy)
                new_end = end_time + duration
                heapq.heappush(busy, (new_end, room))
                counts[room] += 1
            else:
                room = heapq.heappop(available)
                heapq.heappush(busy, (s + duration, room))
                counts[room] += 1
        max_count = max(counts)
        for i, c in enumerate(counts):
            if c == max_count:
                return i