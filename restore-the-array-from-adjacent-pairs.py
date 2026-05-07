from typing import List

class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = {}
        for a, b in adjacentPairs:
            graph.setdefault(a, []).append(b)
            graph.setdefault(b, []).append(a)
        start = next(k for k, v in graph.items() if len(v) == 1)
        res = [start]
        prev = None
        for _ in range(len(adjacentPairs)):
            nxt = next(x for x in graph[res[-1]] if x != prev)
            res.append(nxt)
            prev = res[-2]
        return res
