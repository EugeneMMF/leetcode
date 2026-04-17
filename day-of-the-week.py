class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        def is_leap(y):
            return y % 4 == 0 and (y % 100 != 0 or y % 400 == 0)
        mdays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        offset = 0
        for y in range(1971, year):
            offset += 366 if is_leap(y) else 365
        for m in range(1, month):
            offset += mdays[m - 1]
            if m == 2 and is_leap(year):
                offset += 1
        offset += day - 1
        days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        return days[(5 + offset) % 7]
