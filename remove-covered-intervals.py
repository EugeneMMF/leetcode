class Solution:
    def removeCoveredIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))

        count = 0
        max_r_seen = -1

        for l, r in intervals:
            if r > max_r_seen:
                count += 1
                max_r_seen = r

        return count
