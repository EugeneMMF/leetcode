from typing import List

class Solution:
    def average(self, salary: List[int]) -> float:
        total = sum(salary)
        mn = min(salary)
        mx = max(salary)
        return (total - mn - mx) / (len(salary) - 2)
