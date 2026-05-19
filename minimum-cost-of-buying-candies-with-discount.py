from typing import List

class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse=True)
        total = 0
        n = len(cost)
        i = 0
        while i < n:
            total += cost[i]
            if i + 1 < n:
                total += cost[i + 1]
            i += 3
        return total
