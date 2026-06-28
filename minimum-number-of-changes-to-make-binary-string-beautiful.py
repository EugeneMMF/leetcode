class Solution:
    def minChanges(self, s: str) -> int:
        n = len(s)
        changes = 0
        for i in range(0, n, 2):
            a, b = s[i], s[i + 1]
            cost0 = (a != '0') + (b != '0')
            cost1 = (a != '1') + (b != '1')
            changes += min(cost0, cost1)
        return changes