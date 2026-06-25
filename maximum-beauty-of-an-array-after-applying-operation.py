class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        events = {}
        for x in nums:
            l = x - k
            r = x + k
            events[l] = events.get(l, 0) + 1
            events[r + 1] = events.get(r + 1, 0) - 1
        max_beauty = 0
        current = 0
        for point in sorted(events):
            current += events[point]
            if current > max_beauty:
                max_beauty = current
        return max_beauty
