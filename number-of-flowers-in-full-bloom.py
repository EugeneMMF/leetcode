from bisect import bisect_right, bisect_left
from typing import List

class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        starts = sorted(f[0] for f in flowers)
        ends = sorted(f[1] for f in flowers)
        res = []
        for p in people:
            started = bisect_right(starts, p)
            ended = bisect_left(ends, p)
            res.append(started - ended)
        return res
