class Solution:
    def buttonWithLongestTime(self, events: List[List[int]]) -> int:
        last_time = events[0][1]
        max_time = last_time
        best_idx = events[0][0]
        for idx, t in events[1:]:
            duration = t - last_time
            if duration > max_time or (duration == max_time and idx < best_idx):
                max_time = duration
                best_idx = idx
            last_time = t
        return best_idx
