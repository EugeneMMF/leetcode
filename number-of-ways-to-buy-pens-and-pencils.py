class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        max_p = total // cost1
        ways = 0
        for p in range(max_p + 1):
            remaining = total - p * cost1
            ways += remaining // cost2 + 1
        return ways
