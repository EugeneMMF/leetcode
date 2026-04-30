from typing import List

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        cnt0 = students.count(0)
        cnt1 = len(students) - cnt0
        for s in sandwiches:
            if s == 0:
                if cnt0 == 0:
                    break
                cnt0 -= 1
            else:
                if cnt1 == 0:
                    break
                cnt1 -= 1
        return cnt0 + cnt1
