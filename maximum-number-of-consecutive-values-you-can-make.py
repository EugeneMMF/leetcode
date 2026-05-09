class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        coins.sort()
        reach = 0
        for v in coins:
            if v <= reach + 1:
                reach += v
            else:
                break
        return reach + 1