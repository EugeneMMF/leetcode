class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        if not intervals:
            return 0

        # Sort intervals by their end times.
        # This greedy strategy ensures that we always pick the interval
        # that finishes earliest, leaving the maximum possible room
        # for subsequent non-overlapping intervals.
        intervals.sort(key=lambda x: x[1])

        # Initialize the count of non-overlapping intervals selected.
        # The first interval (after sorting) is always considered non-overlapping with nothing before it.
        count = 1
        # Store the end time of the last chosen non-overlapping interval.
        # We initialize it with the end time of the first interval.
        prev_end = intervals[0][1]

        # Iterate through the rest of the intervals starting from the second one.
        for i in range(1, len(intervals)):
            current_start = intervals[i][0]
            current_end = intervals[i][1]

            # If the current interval's start time is greater than or equal to
            # the end time of the last chosen interval, it means they do not overlap.
            # We can include this interval in our non-overlapping set.
            if current_start >= prev_end:
                count += 1
                prev_end = current_end
        
        # The minimum number of intervals to remove is the total number of intervals
        # minus the maximum number of non-overlapping intervals we found.
        return len(intervals) - count
