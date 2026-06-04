import collections
from typing import List

class Solution:
    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:
        total = collections.defaultdict(int)
        best = {}
        for c, vid, v in zip(creators, ids, views):
            total[c] += v
            if c not in best or v > best[c][0] or (v == best[c][0] and vid < best[c][1]):
                best[c] = (v, vid)
        max_pop = max(total.values())
        res = []
        for c in total:
            if total[c] == max_pop:
                res.append([c, best[c][1]])
        return res
