class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        counts={}
        for i in range(lowLimit, highLimit+1):
            s=sum(int(d) for d in str(i))
            counts[s]=counts.get(s,0)+1
        return max(counts.values())