class UndergroundSystem:
    def __init__(self):
        self.checkins = {}
        self.trips = {}
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkins[id] = (stationName, t)
    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, startTime = self.checkins.pop(id)
        key = (startStation, stationName)
        duration = t - startTime
        if key in self.trips:
            total, cnt = self.trips[key]
            self.trips[key] = (total + duration, cnt + 1)
        else:
            self.trips[key] = (duration, 1)
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total, cnt = self.trips[(startStation, endStation)]
        return total / cnt

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
