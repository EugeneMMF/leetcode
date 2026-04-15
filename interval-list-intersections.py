from typing import List

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i = 0
        j = 0
        res = []
        while i < len(firstList) and j < len(secondList):
            a_start, a_end = firstList[i]
            b_start, b_end = secondList[j]
            start = a_start if a_start > b_start else b_start
            end = a_end if a_end < b_end else b_end
            if start <= end:
                res.append([start, end])
            if a_end < b_end:
                i += 1
            else:
                j += 1
        return res
