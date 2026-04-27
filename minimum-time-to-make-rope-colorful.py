from typing import List

class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        total = 0
        i = 0
        n = len(colors)
        while i < n:
            j = i
            max_time = neededTime[i]
            sum_time = neededTime[i]
            while j + 1 < n and colors[j + 1] == colors[i]:
                j += 1
                sum_time += neededTime[j]
                if neededTime[j] > max_time:
                    max_time = neededTime[j]
            total += sum_time - max_time
            i = j + 1
        return total
