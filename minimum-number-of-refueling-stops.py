class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        import heapq
        max_heap = []
        prev = 0
        fuel = startFuel
        stops = 0
        stations.append([target, 0])
        for position, capacity in stations:
            distance = position - prev
            while fuel < distance:
                if not max_heap:
                    return -1
                fuel += -heapq.heappop(max_heap)
                stops += 1
            fuel -= distance
            prev = position
            heapq.heappush(max_heap, -capacity)
        return stops
