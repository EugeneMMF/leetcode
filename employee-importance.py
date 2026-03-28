from typing import List
import collections

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        employee_map = {}
        for emp in employees:
            employee_map[emp.id] = emp

        total_importance = 0
        q = collections.deque([id])

        while q:
            current_id = q.popleft()
            current_employee = employee_map[current_id]

            total_importance += current_employee.importance

            for sub_id in current_employee.subordinates:
                q.append(sub_id)
        
        return total_importance
