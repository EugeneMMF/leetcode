class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort(key=lambda x: x[0])
        covered = 0
        cur_start, cur_end = meetings[0]
        for s, e in meetings[1:]:
            if s > cur_end + 1:
                covered += cur_end - cur_start + 1
                cur_start, cur_end = s, e
            else:
                if e > cur_end:
                    cur_end = e
        covered += cur_end - cur_start + 1
        return days - covered