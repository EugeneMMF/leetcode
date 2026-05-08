class Solution:
    def minOperations(self, s: str) -> int:
        cost0 = 0
        cost1 = 0
        for i, ch in enumerate(s):
            if i % 2 == 0:
                if ch != '0':
                    cost0 += 1
                if ch != '1':
                    cost1 += 1
            else:
                if ch != '1':
                    cost0 += 1
                if ch != '0':
                    cost1 += 1
        return min(cost0, cost1)
