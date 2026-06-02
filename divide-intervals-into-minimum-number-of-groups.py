class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        events = []
        for l, r in intervals:
            events.append((l, 1))
            events.append((r + 1, -1))
        events.sort()
        cur = 0
        ans = 0
        for _, delta in events:
            cur += delta
            if cur > ans:
                ans = cur
        return ans
