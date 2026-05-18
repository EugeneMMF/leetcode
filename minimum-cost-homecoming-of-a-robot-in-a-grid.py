from typing import List

class Solution:
    def minCost(self, startPos: List[int], homePos: List[int], rowCosts: List[int], colCosts: List[int]) -> int:
        sr, sc = startPos
        hr, hc = homePos
        cost = 0
        if sr < hr:
            cost += sum(rowCosts[sr+1:hr+1])
        elif sr > hr:
            cost += sum(rowCosts[hr:sr])
        if sc < hc:
            cost += sum(colCosts[sc+1:hc+1])
        elif sc > hc:
            cost += sum(colCosts[hc:sc])
        return cost