class Solution:
    def distanceBetweenBusStops(self, distance, start, destination):
        if start > destination:
            start, destination = destination, start
        cw = sum(distance[start:destination])
        return min(cw, sum(distance) - cw)
