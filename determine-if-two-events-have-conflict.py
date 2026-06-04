class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        h1, m1 = map(int, event1[0].split(':'))
        h2, m2 = map(int, event1[1].split(':'))
        s1 = h1 * 60 + m1
        e1 = h2 * 60 + m2
        h3, m3 = map(int, event2[0].split(':'))
        h4, m4 = map(int, event2[1].split(':'))
        s2 = h3 * 60 + m3
        e2 = h4 * 60 + m4
        return max(s1, s2) <= min(e1, e2)
