from typing import List

class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        prev = 0
        best_id = logs[0][0]
        best_duration = logs[0][1] - 0
        prev = logs[0][1]
        for employee, leave in logs[1:]:
            duration = leave - prev
            if duration > best_duration or (duration == best_duration and employee < best_id):
                best_duration = duration
                best_id = employee
            prev = leave
        return best_id
