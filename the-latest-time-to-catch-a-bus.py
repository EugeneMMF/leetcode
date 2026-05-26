class Solution:
    def latestTimeCatchTheBus(self, buses, passengers, capacity):
        buses.sort()
        passengers.sort()
        passenger_set = set(passengers)
        i = 0
        last_bus_time = buses[-1]
        last_bus_full = False
        last_passenger_time = None
        for t in buses:
            count = 0
            while count < capacity and i < len(passengers) and passengers[i] <= t:
                count += 1
                last_passenger_time = passengers[i]
                i += 1
            if t == last_bus_time:
                last_bus_full = (count == capacity)
        if not last_bus_full:
            candidate = last_bus_time
        else:
            candidate = last_passenger_time - 1
        while candidate in passenger_set:
            candidate -= 1
        return candidate