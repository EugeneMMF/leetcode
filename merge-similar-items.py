from typing import List
class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        d={}
        for v,w in items1:
            d[v]=d.get(v,0)+w
        for v,w in items2:
            d[v]=d.get(v,0)+w
        return [[k,d[k]] for k in sorted(d)]