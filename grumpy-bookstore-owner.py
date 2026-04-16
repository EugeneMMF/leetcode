from typing import List

class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        base = 0
        extra = 0
        max_extra = 0
        n = len(customers)
        for i in range(n):
            if grumpy[i] == 0:
                base += customers[i]
            else:
                extra += customers[i]
            if i >= minutes:
                if grumpy[i - minutes] == 1:
                    extra -= customers[i - minutes]
            if i >= minutes - 1 and extra > max_extra:
                max_extra = extra
        return base + max_extra
