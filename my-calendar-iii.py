import collections

class MyCalendarThree:

    def __init__(self):
        self.timeline = collections.defaultdict(int)

    def book(self, startTime: int, endTime: int) -> int:
        self.timeline[startTime] += 1
        self.timeline[endTime] -= 1

        max_k = 0
        current_overlap = 0
        for time_point in sorted(self.timeline.keys()):
            current_overlap += self.timeline[time_point]
            max_k = max(max_k, current_overlap)
        
        return max_k
