from typing import List

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        minutes_list = []
        for time_str in timePoints:
            hours = int(time_str[:2])
            minutes = int(time_str[3:])
            total_minutes = hours * 60 + minutes
            minutes_list.append(total_minutes)

        minutes_list.sort()

        min_diff = float('inf')
        
        for i in range(len(minutes_list) - 1):
            diff = minutes_list[i+1] - minutes_list[i]
            min_diff = min(min_diff, diff)
            if min_diff == 0:
                return 0

        wrap_around_diff = (1440 - minutes_list[-1]) + minutes_list[0]
        min_diff = min(min_diff, wrap_around_diff)

        return min_diff
