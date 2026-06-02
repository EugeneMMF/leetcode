class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        month_days = [31,28,31,30,31,30,31,31,30,31,30,31]
        def to_day(s):
            m=int(s[:2]); d=int(s[3:])
            return sum(month_days[:m-1])+d
        a1=to_day(arriveAlice); l1=to_day(leaveAlice)
        a2=to_day(arriveBob); l2=to_day(leaveBob)
        start=max(a1,a2); end=min(l1,l2)
        return max(0,end-start+1)
