class Solution:
    def minOperationsMaxProfit(self, customers, boardingCost, runningCost):
        waiting = 0
        profit = 0
        maxProfit = 0
        bestRot = -1
        i = 0
        rotations = 0
        n = len(customers)
        while i < n or waiting > 0:
            if i < n:
                waiting += customers[i]
                i += 1
            board = 4 if waiting >= 4 else waiting
            waiting -= board
            profit += board * boardingCost - runningCost
            rotations += 1
            if profit > maxProfit:
                maxProfit = profit
                bestRot = rotations
        return bestRot if maxProfit > 0 else -1
