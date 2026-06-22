from typing import List

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        setA = set()
        setB = set()
        res = []
        for a, b in zip(A, B):
            setA.add(a)
            setB.add(b)
            res.append(len(setA & setB))
        return res
