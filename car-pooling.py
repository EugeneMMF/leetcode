class Solution:
    def carPooling(self, trips, capacity):
        changes = {}
        for num, start, end in trips:
            changes[start] = changes.get(start, 0) + num
            changes[end] = changes.get(end, 0) - num
        cur = 0
        for loc in sorted(changes):
            cur += changes[loc]
            if cur > capacity:
                return False
        return True
