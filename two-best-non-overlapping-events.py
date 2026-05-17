class Solution:
    def maxTwoEvents(self, events):
        import bisect
        max_single = 0
        for s, e, v in events:
            if v > max_single:
                max_single = v
        ends_sorted = sorted(events, key=lambda x: x[1])
        ends = [e for s, e, v in ends_sorted]
        pref = [0] * len(events)
        pref[0] = ends_sorted[0][2]
        for i in range(1, len(events)):
            pref[i] = pref[i - 1] if pref[i - 1] > ends_sorted[i][2] else ends_sorted[i][2]
        events_sorted = sorted(events, key=lambda x: x[0])
        max_two = 0
        for s, e, v in events_sorted:
            idx = bisect.bisect_left(ends, s) - 1
            if idx >= 0:
                best_before = pref[idx]
                if v + best_before > max_two:
                    max_two = v + best_before
        return max_single if max_single > max_two else max_two
