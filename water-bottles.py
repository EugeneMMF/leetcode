class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        total = numBottles
        empty = numBottles
        while empty >= numExchange:
            exchange = empty // numExchange
            total += exchange
            empty = empty % numExchange + exchange
        return total
