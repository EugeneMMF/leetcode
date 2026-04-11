class Solution:
    def numBusesToDestination(self, routes, source, target):
        if source == target:
            return 0
        from collections import defaultdict, deque
        stop_to_buses = defaultdict(list)
        for i, r in enumerate(routes):
            for s in r:
                stop_to_buses[s].append(i)
        if source not in stop_to_buses or target not in stop_to_buses:
            return -1
        visited_buses = set()
        visited_stops = set([source])
        q = deque()
        for b in stop_to_buses[source]:
            q.append((b, 1))
            visited_buses.add(b)
        while q:
            bus, cnt = q.popleft()
            for stop in routes[bus]:
                if stop == target:
                    return cnt
                for nb in stop_to_buses[stop]:
                    if nb not in visited_buses:
                        visited_buses.add(nb)
                        q.append((nb, cnt + 1))
        return -1
