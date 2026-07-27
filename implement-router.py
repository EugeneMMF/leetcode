class Router:

    def __init__(self, memoryLimit: int):
        from collections import deque
        self.memoryLimit = memoryLimit
        self.queue = deque()
        self.packet_set = set()
        self.dest_timestamps = {}
        self.dest_index = {}

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        key = (source, destination, timestamp)
        if key in self.packet_set:
            return False
        if len(self.queue) == self.memoryLimit:
            old = self.queue.popleft()
            self.packet_set.remove((old[0], old[1], old[2]))
            dest = old[1]
            self.dest_index[dest] = self.dest_index.get(dest, 0) + 1
        self.queue.append((source, destination, timestamp))
        self.packet_set.add(key)
        if destination not in self.dest_timestamps:
            self.dest_timestamps[destination] = []
            self.dest_index[destination] = 0
        self.dest_timestamps[destination].append(timestamp)
        return True

    def forwardPacket(self) -> List[int]:
        if not self.queue:
            return []
        src, dest, ts = self.queue.popleft()
        self.packet_set.remove((src, dest, ts))
        self.dest_index[dest] = self.dest_index.get(dest, 0) + 1
        return [src, dest, ts]

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        from bisect import bisect_left, bisect_right
        lst = self.dest_timestamps.get(destination, [])
        idx = self.dest_index.get(destination, 0)
        if idx >= len(lst):
            return 0
        left = bisect_left(lst, startTime, idx)
        right = bisect_right(lst, endTime, idx)
        return right - left

# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)