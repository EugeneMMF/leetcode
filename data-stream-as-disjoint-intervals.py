class SummaryRanges:

    def __init__(self):
        self.nums = set()

    def addNum(self, value: int) -> None:
        self.nums.add(value)

    def getIntervals(self) -> list[list[int]]:
        if not self.nums:
            return []

        sorted_nums = sorted(list(self.nums))
        
        intervals = []
        current_start = sorted_nums[0]
        current_end = sorted_nums[0]

        for i in range(1, len(sorted_nums)):
            num = sorted_nums[i]
            if num == current_end + 1:
                current_end = num
            else:
                intervals.append([current_start, current_end])
                current_start = num
                current_end = num
        
        intervals.append([current_start, current_end])
        return intervals
