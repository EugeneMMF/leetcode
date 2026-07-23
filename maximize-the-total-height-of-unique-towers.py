class Solution:
    def maximumTotalSum(self, maximumHeight: List[int]) -> int:
        maximumHeight.sort(reverse=True)
        current = 10**18
        total = 0
        for h in maximumHeight:
            if current > h:
                current = h
            else:
                current -= 1
            if current <= 0:
                return -1
            total += current
        return total
