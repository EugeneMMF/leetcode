import collections

class MyCalendarTwo:

    def __init__(self):
        self.deltas = collections.defaultdict(int)

    def book(self, startTime: int, endTime: int) -> bool:
        temp_deltas = self.deltas.copy()
        temp_deltas[startTime] += 1
        temp_deltas[endTime] -= 1

        active_bookings = 0
        for time_point in sorted(temp_deltas.keys()):
            active_bookings += temp_deltas[time_point]
            if active_bookings >= 3:
                return False
        
        self.deltas = temp_deltas
        return True

