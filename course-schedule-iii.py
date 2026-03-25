import heapq

class Solution:
    def scheduleCourse(self, courses: list[list[int]]) -> int:
        courses.sort(key=lambda x: x[1])

        current_time = 0
        taken_durations = []

        for duration, last_day in courses:
            current_time += duration
            heapq.heappush(taken_durations, -duration)

            if current_time > last_day:
                longest_duration = -heapq.heappop(taken_durations)
                current_time -= longest_duration
        
        return len(taken_durations)
