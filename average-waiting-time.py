from typing import List

class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        cur = 0
        total = 0
        for arr, t in customers:
            start = cur if cur > arr else arr
            cur = start + t
            total += cur - arr
        return total / len(customers)
