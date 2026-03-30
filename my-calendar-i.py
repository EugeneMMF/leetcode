class MyCalendar:

    def __init__(self):
        self.calendar = []

    def book(self, startTime: int, endTime: int) -> bool:
        for existing_start, existing_end in self.calendar:
            if startTime < existing_end and existing_start < endTime:
                return False
        
        self.calendar.append((startTime, endTime))
        return True
