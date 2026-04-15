from typing import List

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        indeg = [0] * (n + 1)
        outdeg = [0] * (n + 1)
        for a, b in trust:
            outdeg[a] += 1
            indeg[b] += 1
        for i in range(1, n + 1):
            if outdeg[i] == 0 and indeg[i] == n - 1:
                return i
        return -1
