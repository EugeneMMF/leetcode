class Solution:
    def twoEggDrop(self, n: int) -> int:
        k=0
        s=0
        while s<n:
            k+=1
            s+=k
        return k
