class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        y1, m1, d1 = map(int, date1.split('-'))
        y2, m2, d2 = map(int, date2.split('-'))
        from datetime import date
        return abs((date(y2, m2, d2) - date(y1, m1, d1)).days)
