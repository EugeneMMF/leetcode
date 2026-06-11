from typing import List

class Solution:
    def findMinimumTime(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda x: x[1])
        chosen = [False] * 2001
        total = 0
        for s, e, d in tasks:
            count = 0
            for t in range(s, e + 1):
                if chosen[t]:
                    count += 1
            need = d - count
            t = e
            while need > 0:
                while t >= s and chosen[t]:
                    t -= 1
                if t < s:
                    break
                chosen[t] = True
                total += 1
                need -= 1
                t -= 1
        return total
