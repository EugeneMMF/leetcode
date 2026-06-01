class Solution:
    def taskSchedulerII(self, tasks, space):
        last_day = {}
        current_day = 0
        for t in tasks:
            earliest = current_day
            if t in last_day:
                earliest = max(earliest, last_day[t] + space + 1)
            last_day[t] = earliest
            current_day = earliest + 1
        return current_day