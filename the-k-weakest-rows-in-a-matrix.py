from typing import List

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        res=[]
        for i,row in enumerate(mat):
            lo,hi=0,len(row)
            while lo<hi:
                mid=(lo+hi)//2
                if row[mid]==1:
                    lo=mid+1
                else:
                    hi=mid
            res.append((lo,i))
        res.sort()
        return [idx for _,idx in res[:k]]
