from typing import List

class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        total = 0
        cur = 0
        for i in range(len(satisfaction) - 1, -1, -1):
            total += satisfaction[i]
            if total > 0:
                cur += total
            else:
                break
        return cur
