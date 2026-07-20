from typing import List
from math import isqrt

class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        freq={}
        for v in nums2:
            freq[v]=freq.get(v,0)+1
        total=0
        for x in nums1:
            if x%k: continue
            t=x//k
            r=isqrt(t)
            for d in range(1,r+1):
                if t%d==0:
                    total+=freq.get(d,0)
                    other=t//d
                    if other!=d:
                        total+=freq.get(other,0)
        return total
